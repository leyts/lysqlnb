from enum import IntEnum, StrEnum, auto

from pydantic import BaseModel, ConfigDict, Field


class CellKind(IntEnum):
    """Notebook cell types matching VS Code's notebook format."""

    MARKDOWN = 1
    CODE = 2


class TrailingNewlines(StrEnum):
    """Trailing newline normalisation modes."""

    PRESERVE = auto()
    NONE = auto()
    ONE = auto()


class Cell(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kind: CellKind
    value: str
    language_id: str = Field(alias="languageId")


class Notebook(BaseModel):
    model_config = ConfigDict(extra="forbid")

    cells: list[Cell]
