import os
import sqlite3

from platformdirs import user_data_dir

__version__ = "0.3.2"

DATABASE_PATH = os.path.join(
    user_data_dir(appname="graphreveal", appauthor="graphreveal"), "graphs.db"
)


class ParsingError(Exception):
    def __init__(self, message: str, errors_coordinates: list[tuple[int, int, int]]):
        self.message = message
        self.errors_coordinates = set()
        for line, column, length in errors_coordinates:
            for i in range(length):
                self.errors_coordinates.add((line - 1, column + i))


def get_ids(sql_query: str) -> list[str]:
    sql_query = sql_query.replace("*", "id", 1)
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()

    result = cur.execute(sql_query).fetchall()
    return [graph_id for (graph_id,) in result]
