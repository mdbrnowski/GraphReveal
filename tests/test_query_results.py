import pytest
import sqlite3
from ..translator.translate import translate


@pytest.mark.parametrize('query,expected_count', [
    ('1 vertex', 1),
    ('2 vertices', 2),
    ('6 vertices, connected', 112),
    ('6 vertices, connected, not 15 edges', 111),
    ('6 vertices, connected, not complete', 111),
    ('1 edge, connected', 1),
    ('3 edges, connected', 3),
    ('6 edges, connected', 30),
    ('!bipartite, acyclic', 0),
    ('5 vertices, complete', 1),
    ('7 vertices, eulerian', 37),
    ('5 vertices, connected, planar', 20),
    ('5 vertices, tree', 3),
    ('5 vertices, 2 components', 8),
])
def test_query_results(query, expected_count):
    sql_query = translate(query)

    con = sqlite3.connect("graphs.db")
    cur = con.cursor()

    print(sql_query)

    result = cur.execute(sql_query)
    assert len(result.fetchall()) == expected_count
