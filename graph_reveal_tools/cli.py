import typer
from graph_reveal_tools import get_ids
from graph_reveal_tools.translator import translate

app = typer.Typer()


@app.command()
def main(query: str, count: bool = False, sql: bool = False):
    """
    Get all graphs with given properties.

    Currently, graphs with up to 7 vertices are considered.
    """
    if count:
        print(len(get_ids(translate(query))))
    elif sql:
        print(translate(query))
    else:
        print('\n'.join(get_ids(translate(query))))


if __name__ == '__main__':
    app()
