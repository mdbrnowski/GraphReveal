import pytest
from antlr4 import *

from ..translator.generated.QueryLexer import QueryLexer
from ..translator.generated.QueryParser import QueryParser


@pytest.mark.parametrize("valid_query", [
    "6 vertices",
    "18 edges",
    "2 components",
    "1 vertex; 1 edge; 1 component",
    "2 V, 0 E, 1 C",
    "not acyclic, ! bipartite, connected, eulerian",
    "5 V; !planar",
    "6 vertices, not complete",
    "not 2 vertices, 1 edge",
])
def test_valid_query(valid_query):
    lexer = QueryLexer(InputStream(valid_query))
    parser = QueryParser(CommonTokenStream(lexer))

    parser.query()
    assert parser.getNumberOfSyntaxErrors() == 0


@pytest.mark.parametrize("invalid_query", [
    "",
    "1",
    ","
    "wrong",
    "vertices",
    "edges",
    "component",
    "1 bipartite",
    "bipartite 1",
    "6 vertices ,, 8 edges"
])
def test_invalid_query(invalid_query):
    lexer = QueryLexer(InputStream(invalid_query))
    parser = QueryParser(CommonTokenStream(lexer))

    parser.query()
    assert parser.getNumberOfSyntaxErrors() > 0
