import pytest
from typer.testing import CliRunner

from graphreveal.cli import app

runner = CliRunner()


def test_app_search():
    result = runner.invoke(app, ["search", "1 vertex"])
    assert result.exit_code == 0
    assert result.stdout == "@\n"
    assert result.stderr == ""


def test_app_count():
    result = runner.invoke(app, ["count", "6 vertices, connected"])
    assert result.exit_code == 0
    assert result.stdout == "112\n"
    assert result.stderr == ""


def test_app_sql():
    result = runner.invoke(app, ["to-sql", "5 vertices, planar"])
    assert result.exit_code == 0
    assert (
        result.stdout == "SELECT * FROM graphs WHERE vertices = 5 AND planar = TRUE\n"
    )
    assert result.stderr == ""


@pytest.mark.parametrize("command", ["search", "count", "to-sql"])
def test_app_lexer_error(command):
    result = runner.invoke(app, [command, "invalid"])
    assert result.exit_code == 2


@pytest.mark.parametrize("command", ["search", "count", "to-sql"])
def test_app_parser_error(command):
    result = runner.invoke(app, [command, "vertices"])
    assert result.exit_code == 2


def test_create_database_error_too_small():
    result = runner.invoke(app, ["create-database", "--n", "0"])
    assert result.exit_code == 1


def test_create_database_error_too_large():
    result = runner.invoke(app, ["create-database", "--n", "10"])
    assert result.exit_code == 1
