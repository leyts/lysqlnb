"""Notebook data models."""

from enum import IntEnum, StrEnum

from pydantic import BaseModel, ConfigDict, Field


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
        kind: Kind of cell data.
        value: Source value of this cell data — either
            source code or markup text.
        language_id: Language identifier of the source
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
        cells: Cell data of this notebook.
    """

    model_config = ConfigDict(extra="forbid")

    cells: list[NotebookCell]
