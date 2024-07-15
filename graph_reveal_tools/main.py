import sqlite3


def get_ids(sql_query: str) -> list[str]:
    sql_query = sql_query.replace('*', 'id', 1)
    con = sqlite3.connect('graphs.db')
    cur = con.cursor()

    result = cur.execute(sql_query).fetchall()
    return [graph_id for (graph_id,) in result]
