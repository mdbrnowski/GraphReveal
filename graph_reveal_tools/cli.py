import typer
from graph_reveal_tools.translator import translate

app = typer.Typer()


@app.command()
def main(query: str, count: bool = False, sql: bool = False):
    """
    Get all graphs with given properties.

    Currently, graphs with up to 7 vertices are considered.
    """
    # todo
    if count:
        print('Number of graphs with given properties.')
    elif sql:
        print(translate(query))
    else:
        print(f'Search results for "{translate(query)}".')


if __name__ == '__main__':
    app()
