import pytest
from graphreveal import get_ids
from graphreveal.translator import translate


@pytest.mark.parametrize(
    "query,expected_count",
    [
        ("1 vertex", 1),
        ("2 vertices", 2),
        ("6 vertices, connected", 112),
        ("6 vertices, connected, not 15 edges", 111),
        ("6 vertices, connected, not complete", 111),
        ("1 edge, connected", 1),
        ("3 edges, connected", 3),
        ("6 edges, connected", 30),
        ("!bipartite, acyclic", 0),
        ("5 vertices, complete", 1),
        ("7 vertices, eulerian", 37),
        ("5 vertices, connected, planar", 20),
        ("5 vertices, tree", 3),
        ("3 vertices, not tree", 3),
        ("5 vertices, 2 components", 8),
        ("3 edges, no isolated vertices", 5),
        ("1 vertex, hamiltonian", 1),
        ("2 vertices, hamiltonian", 0),
        ("3 vertices, hamiltonian", 1),
        ("4 vertices, hamiltonian", 3),
        ("5 vertices, hamiltonian", 8),
        ("6 vertices, hamiltonian", 48),
        ("7 vertices, hamiltonian", 383),
        ("5 vertices, connected, 2 blocks", 5),
        ("5 vertices, connected, 1 block", 10),
        ("4 vertices, cubic", 1),
        ("5 vertices, cubic", 0),
        ("6 vertices, trivalent", 2),
        ("4 vertices, connected, regular", 2),
        ("2..4 vertices, connected", 1 + 2 + 6),
        ("<=4 vertices, connected", 1 + 1 + 2 + 6),
        ("1-3 edges, no isolated vertices", 1 + 2 + 5),
        ("4 vertices, >2 components", 2),
        ("3 vertices, >=2 components", 2),
        ("4 vertices, connected, <3 blocks, >1 block", 1),
    ],
)
def test_query_results(query, expected_count):
    sql_query = translate(query)
    assert len(get_ids(sql_query)) == expected_count
