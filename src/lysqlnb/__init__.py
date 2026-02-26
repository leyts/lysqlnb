"""lysqlnb — a library for reading and validating SQL notebook files."""

from typing import TYPE_CHECKING

from lysqlnb.exceptions import NotebookParseError
from lysqlnb.models import (
    Notebook,
    NotebookCell,
    NotebookCellKind,
    NotebookCellLanguage,
)
from lysqlnb.reader import reads as _reads

if TYPE_CHECKING:
    from pathlib import Path

__all__ = [
    "Notebook",
    "NotebookCell",
    "NotebookCellKind",
    "NotebookCellLanguage",
    "NotebookParseError",
    "read",
    "reads",
]


def reads(s: str) -> Notebook:
    """Read a notebook from a string and return the Notebook object.

    Args:
        s: String to read the notebook from.

    Returns:
        Notebook data object.

    Raises:
        NotebookParseError: If the string contains invalid YAML or
            does not conform to the notebook schema.
    """
    return _reads(s)


def read(path: Path) -> Notebook:
    """Read a notebook from a file path.

    Args:
        path: Path to the notebook file.

    Returns:
        Notebook data object.

    Raises:
        NotebookParseError: If the file contains invalid YAML or
            does not conform to the notebook schema.
    """
    return reads(path.read_text(encoding="utf-8"))
