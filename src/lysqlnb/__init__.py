"""lysqlnb package."""

from typing import TYPE_CHECKING

from lysqlnb._loader import _loads
from lysqlnb._models import (
    Notebook,
    NotebookCell,
    NotebookCellKind,
    NotebookCellLanguage,
)
from lysqlnb.exceptions import NotebookParseError

if TYPE_CHECKING:
    from pathlib import Path

__all__ = [
    "Notebook",
    "NotebookCell",
    "NotebookCellKind",
    "NotebookCellLanguage",
    "NotebookParseError",
    "load",
    "loads",
]


def loads(s: str) -> Notebook:
    """Load a notebook from a string.

    Args:
        s: String to load the notebook from.

    Returns:
        Notebook data object.

    Raises:
        NotebookParseError: If the string contains invalid YAML or
            does not conform to the notebook schema.
    """
    return _loads(s)


def load(path: Path) -> Notebook:
    """Load a notebook from a file path.

    Args:
        path: Path to the notebook file.

    Returns:
        Notebook data object.

    Raises:
        NotebookParseError: If the file contains invalid YAML or
            does not conform to the notebook schema.
    """
    return loads(path.read_text(encoding="utf-8"))
