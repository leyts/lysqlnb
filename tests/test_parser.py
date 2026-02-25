from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


def parse_notebook(path: Path) -> list[str]:
    """Stub for the library's parsing function."""
    raise NotImplementedError


def test_parse_notebook(shared_datadir: Path) -> None:
    cells: list[str] = parse_notebook(shared_datadir / "test_notebook.sqlnb")

    assert cells == [
        "# This is Markdown.",
        (
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
        ),
    ]
