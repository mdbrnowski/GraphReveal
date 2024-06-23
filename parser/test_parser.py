import pytest
from antlr4 import *

from QueryLexer import QueryLexer
from QueryParser import QueryParser


@pytest.mark.parametrize("valid_query", [
    "6 vertices",
    "18 edges",
    "1 vertex; 1 edge",
    "2 V, 0 E",
    "not acyclic, ! bipartite, connected, eulerian",
    "5 V; !planar",
])
def test_valid_query(valid_query):
    lexer = QueryLexer(InputStream(valid_query))
    parser = QueryParser(CommonTokenStream(lexer))

    tree = parser.query()
    assert parser._syntaxErrors == 0


@pytest.mark.parametrize("invalid_query", [
    "wrong",
    "vertices",
    "edges",
    "1 bipartite",
])
def test_invalid_query(invalid_query):
    lexer = QueryLexer(InputStream(invalid_query))
    parser = QueryParser(CommonTokenStream(lexer))

    tree = parser.query()
    assert parser._syntaxErrors > 0
