import os
from sqlite3 import OperationalError

import rich
import typer
from rich.prompt import Confirm

from graphreveal import get_ids, ParsingError, DATABASE_PATH
from graphreveal.db_creator import create_db
from graphreveal.translator import translate

app = typer.Typer(no_args_is_help=True)


def _print_parsing_error(query: str, e: ParsingError):
    rich.print("[bold red]Query error:\n")
    for i, query_line in enumerate(query.split("\n"), start=1):
        query_line += " "
        if i == e.error_line:
            rich.print(
                f"  [not bold cyan]{query_line[: e.error_column]}"
                f"[bold red]{query_line[e.error_column : e.error_column + e.error_length]}"
                f"[not bold cyan]{query_line[e.error_column + e.error_length :]}"
            )
            rich.print(f"  {' ' * e.error_column}[red]{'^' * e.error_length}")
        else:
            rich.print(f"  [not bold cyan]{query_line}\n")
    rich.print()


@app.command()
def search(query: str, count: bool = False):
    """
    Get all graphs with given properties.
    """
    try:
        sql_query = translate(query)
        if count:
            print(len(get_ids(sql_query)))
        else:
            print("\n".join(get_ids(sql_query)))
    except ParsingError as e:
        _print_parsing_error(query, e)
    except OperationalError as e:
        rich.print("[bold red]Error:", str(e) + ".")
        rich.print(
            "Try to create the database first. Run `[cyan]graphreveal create-database[/cyan]`."
        )


@app.command()
def create_database(n: int = 7):
    """
    Create the database.
    """
    if n > 9 or n < 1:
        rich.print("[bold red]Error: Choose n between 1 and 9.")
        return

    try:
        if not os.path.exists(DATABASE_PATH) or Confirm.ask(
            "Are you sure you want to overwrite the database?"
        ):
            create_db(n)
    except OperationalError as e:
        rich.print("[bold red]Error:", str(e) + ".")


@app.command()
def to_sql(query: str):
    """
    Translate your query to SQL.
    """
    try:
        sql_query = translate(query)
        print(sql_query)
    except ParsingError as e:
        _print_parsing_error(query, e)


if __name__ == "__main__":
    app()
