from typing import TYPE_CHECKING

import pytest

from lysqlnb.models import NotebookCellKind, NotebookCellLanguage, NotebookData

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def notebook(shared_datadir: Path) -> NotebookData:
    return NotebookData.from_file(shared_datadir / "test_notebook.sqlnb")


def test_notebook_cell_count(notebook: NotebookData):
    assert len(notebook.cells) == 2


def test_notebook_cell_kind(notebook: NotebookData):
    assert notebook.cells[0].kind == NotebookCellKind.MARKUP
    assert notebook.cells[1].kind == NotebookCellKind.CODE


def test_notebook_cell_value(notebook: NotebookData):
    assert notebook.cells[0].value == "# This is Markdown."
    assert notebook.cells[1].value == (
        "-- This is SQL.\n"
        "SELECT\n"
        "    department_id,\n"
        "    AVG(salary) AS avg_salary\n"
        "FROM\n"
        "    employees\n"
        "GROUP BY\n"
        "    department_id\n"
        "HAVING\n"
        "    AVG(salary) > 5000;"
    )


def test_notebook_cell_value_blank(shared_datadir: Path):
    notebook: NotebookData = NotebookData.from_file(
        shared_datadir / "test_notebook_blank_cell.sqlnb"
    )
    assert notebook.cells[0].value == "# The cell below is blank."
    assert notebook.cells[1].value == ""
    assert notebook.cells[2].value == "# The cell above is blank."


def test_notebook_cell_language(notebook: NotebookData):
    assert notebook.cells[0].language_id == NotebookCellLanguage.MARKDOWN
    assert notebook.cells[1].language_id == NotebookCellLanguage.ORACLE_SQL
