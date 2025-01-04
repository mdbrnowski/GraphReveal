import sqlite3

from graphreveal_tools import DATABASE_PATH


class ParsingError(Exception):
    pass


def get_ids(sql_query: str) -> list[str]:
    sql_query = sql_query.replace('*', 'id', 1)
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()

    result = cur.execute(sql_query).fetchall()
    return [graph_id for (graph_id,) in result]
