from typer.testing import CliRunner
from graphreveal.cli import app

runner = CliRunner()


def test_app_search():
    result = runner.invoke(app, ["search", "1 vertex"])
    assert result.exit_code == 0
    assert result.output == "@\n"


def test_app_count():
    result = runner.invoke(app, ["count", "6 vertices, connected"])
    assert result.exit_code == 0
    assert result.stdout == "112\n"


def test_app_sql():
    result = runner.invoke(app, ["to-sql", "5 vertices, planar"])
    assert result.exit_code == 0
    assert (
        result.stdout == "SELECT * FROM graphs WHERE vertices = 5 AND planar = TRUE\n"
    )
