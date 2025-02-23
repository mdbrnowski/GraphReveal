import pytest
from antlr4 import InputStream, CommonTokenStream

from graphreveal.translator import QueryLexer, QueryParser


@pytest.mark.parametrize(
    "valid_query",
    [
        "6 vertices",
        "18 edges",
        "2 components",
        "100 nodes",
        "1 vertex; 1 edge; 1 component; 1 node",
        "2 V, 0 E, 1 C",
        "not acyclic, ! bipartite, connected, eulerian",
        "hamiltonian, euler, hamilton",
        "5 V; !planar",
        "6 vertices, not complete",
        "not 2 vertices, 1 edge",
        "forest; tree; no isolated vertices",
        "2 biconnected components, 2 blocks",
        "3..5 vertices, >6 edges",
        "<6 vertices, 7-9 edges",
        "<=5 vertices, 7..9 edges",
        "<=2 vertices, >=11 edges",
    ],
)
def test_valid_query(valid_query):
    lexer = QueryLexer(InputStream(valid_query))
    parser = QueryParser(CommonTokenStream(lexer))

    parser.query()
    assert parser.getNumberOfSyntaxErrors() == 0


@pytest.mark.parametrize(
    "invalid_query",
    [
        "",
        "1",
        ",",
        "wrong",
        "vertices",
        "edges",
        "component",
        "1 bipartite",
        "bipartite 1",
        "6 vertices ,, 8 edges",
        "6 V 8 E",
        "isolated vertices",
        "biconnected component component",
        "5 vertices, 8 eulerian",
        "6 vertices, < edges",
        "5 vertices, .. edges,",
    ],
)
def test_invalid_query(invalid_query):
    lexer = QueryLexer(InputStream(invalid_query))
    parser = QueryParser(CommonTokenStream(lexer))

    parser.query()
    assert parser.getNumberOfSyntaxErrors() > 0
