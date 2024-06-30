import pytest
import sqlite3
from ..translator.translate import translate


@pytest.mark.parametrize('query,expected_count', [
    ('6 vertices, connected', 112),
    ('!bipartite, acyclic', 0),
])
def test_query_results(query, expected_count):
    sql_query = translate(query)

    con = sqlite3.connect("graphs.db")
    cur = con.cursor()

    print(sql_query)

    result = cur.execute(sql_query)
    assert len(result.fetchall()) == expected_count
