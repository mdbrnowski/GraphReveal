from sqlite3 import OperationalError

import rich
import typer

from graph_reveal_tools.main import get_ids
from graph_reveal_tools.db_creator import create_db
from graph_reveal_tools.translator import translate

app = typer.Typer(no_args_is_help=True)


@app.command()
def search(query: str, count: bool = False):
    """
    Get all graphs with given properties.
    """
    sql_query = translate(query)
    try:
        if count:
            print(len(get_ids(sql_query)))
        else:
            print('\n'.join(get_ids(sql_query)))
    except OperationalError as e:
        rich.print('[bold red]Error:', str(e) + '.')
        rich.print('Try to create the database first. Run `[cyan]graph-reveal create-database[/cyan]`.')


@app.command()
def create_database(n: int = 7):
    """
    Create the database.
    """
    if n > 9 or n < 1:
        rich.print('[bold red]Error: Choose n between 1 and 9.')
        return

    try:
        create_db(n)
    except OperationalError as e:
        rich.print('[bold red]Error:', str(e) + '.')


@app.command()
def to_sql(query: str):
    """
    Translate your query to SQL.
    """
    sql_query = translate(query)
    print(sql_query)


if __name__ == '__main__':
    app()
