"""Notebook data models and parsing."""

from enum import IntEnum, StrEnum
from typing import TYPE_CHECKING, Any

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from lysqlnb.exceptions import NotebookParseError

if TYPE_CHECKING:
    from pathlib import Path


class NotebookCellKind(IntEnum):
    """A notebook cell kind.

    Attributes:
        MARKUP: Formatted source that is used for display.
        CODE: Source that can be executed and that produces output.
    """

    MARKUP = 1
    CODE = 2


class NotebookCellLanguage(StrEnum):
    """Language identifier for a notebook cell.

    Attributes:
        MARKDOWN: Markdown markup language.
        ORACLE_SQL: Oracle SQL dialect.
    """

    MARKDOWN = "markdown"
    ORACLE_SQL = "oracle-sql"


class NotebookCell(BaseModel):
    """Raw representation of a notebook cell.

    Attributes:
        kind: The kind of cell data.
        value: The source value of this cell data — either
            source code or formatted text.
        language_id: The language identifier of the source
            value of this cell data.
    """

    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    kind: NotebookCellKind
    value: str
    language_id: NotebookCellLanguage = Field(alias="languageId")

    def __str__(self) -> str:
        """Return the cell's value as its string representation."""
        return self.value


class Notebook(BaseModel):
    """Raw representation of a notebook.

    Attributes:
        cells: The cell data of this notebook.
    """

    model_config = ConfigDict(extra="forbid")

    cells: list[NotebookCell]

    @classmethod
    def from_file(cls, path: Path) -> Notebook:
        """Create a notebook from a file.

        Args:
            path: Path to the notebook file.

        Returns:
            A validated notebook data object.

        Raises:
            NotebookParseError: If the file contains invalid YAML or
                does not conform to the notebook schema.
        """
        try:
            raw: Any = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            msg = f"Invalid YAML: {e}"
            raise NotebookParseError(msg) from e

        try:
            return cls.model_validate(raw)
        except ValidationError as e:
            msg = f"Invalid notebook structure: {e}"
            raise NotebookParseError(msg) from e
