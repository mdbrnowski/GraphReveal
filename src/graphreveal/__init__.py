import os
import sqlite3

from platformdirs import user_data_dir

DATABASE_PATH = os.path.join(
    user_data_dir(appname="graphreveal", appauthor="graphreveal"), "graphs.db"
)


class ParsingError(Exception):
    def __init__(self, message: str, errors_coordinates: list[tuple[int, int, int]]):
        # todo: show all errors, not just the first one
        error_coordinates = errors_coordinates[0]
        self.message = message
        self.error_line, self.error_column, self.error_length = error_coordinates


def get_ids(sql_query: str) -> list[str]:
    sql_query = sql_query.replace("*", "id", 1)
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()

    result = cur.execute(sql_query).fetchall()
    return [graph_id for (graph_id,) in result]
