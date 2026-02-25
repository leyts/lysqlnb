from typing import TYPE_CHECKING

import yaml
from pydantic import ValidationError

from lysqlnb.models import Notebook

if TYPE_CHECKING:
    from pathlib import Path


class NotebookParseError(Exception):
    """Raised when a notebook file cannot be parsed."""


def parse_notebook(path: Path) -> Notebook:
    try:
        data = yaml.safe_load(path.read_text())
    except yaml.YAMLError as e:
        msg = f"Invalid YAML: {e}"
        raise NotebookParseError(msg) from e

    try:
        return Notebook.model_validate(data)
    except ValidationError as e:
        msg = f"Invalid notebook structure: {e}"
        raise NotebookParseError(msg) from e
