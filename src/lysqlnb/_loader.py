"""YAML parsing and validation for notebook files."""

from typing import Any

import yaml
from pydantic import ValidationError

from lysqlnb._models import Notebook
from lysqlnb.exceptions import NotebookParseError


def _loads(s: str) -> Notebook:
    """Load a raw YAML string into a notebook.

    Args:
        s: YAML string to load.

    Returns:
        Notebook data object.

    Raises:
        NotebookParseError: If the string contains invalid YAML or
            does not conform to the notebook schema.
    """
    try:
        raw: Any = yaml.safe_load(s)
    except yaml.YAMLError as e:
        msg = f"Invalid YAML: {e}"
        raise NotebookParseError(msg) from e

    try:
        return Notebook.model_validate(raw)
    except ValidationError as e:
        msg = f"Invalid notebook structure: {e}"
        raise NotebookParseError(msg) from e
