from typer.testing import CliRunner
from graph_reveal_tools.cli import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ['1 vertex'])
    assert result.exit_code == 0
    assert result.output == '@\n'


def test_app_with_count():
    result = runner.invoke(app, ['6 vertices, connected', '--count'])
    assert result.exit_code == 0
    assert result.stdout == '112\n'


def test_app_with_sql():
    result = runner.invoke(app, ['5 vertices, planar', '--sql'])
    assert result.exit_code == 0
    assert result.stdout == 'SELECT * FROM graphs WHERE vertices = 5 AND planar = TRUE\n'


def test_app_with_count_and_sql():
    result = runner.invoke(app, ['2 vertices', '--count', '--sql'])
    assert result.exit_code == 0
    assert result.stdout == '2\nSELECT * FROM graphs WHERE vertices = 2\n'
