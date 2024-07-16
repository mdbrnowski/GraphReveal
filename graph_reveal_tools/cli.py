import typer
from graph_reveal_tools import get_ids
from graph_reveal_tools.translator import translate

app = typer.Typer()


@app.command()
def search(query: str, count: bool = False, sql: bool = False):
    """
    Get all graphs with given properties.

    Currently, graphs with up to 7 vertices are considered.
    """
    sql_query = translate(query)
    if count or sql:
        if count:
            print(len(get_ids(sql_query)))
        if sql:
            print(sql_query)
    else:
        print('\n'.join(get_ids(sql_query)))


if __name__ == '__main__':
    app()
