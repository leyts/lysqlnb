from typing import TYPE_CHECKING

from lysqlnb.models import TrailingNewlines

if TYPE_CHECKING:
    from pathlib import Path


def normalise_trailing_newlines(content: str, mode: TrailingNewlines) -> str:
    """Normalise trailing newlines in content.

    Args:
        content: The content to normalise.
        mode: The normalisation mode to apply.

    Returns:
        The content with trailing newlines normalised according to mode.
    """
    match mode:
        case TrailingNewlines.PRESERVE:
            return content
        case TrailingNewlines.NONE:
            return content.rstrip("\n")
        case TrailingNewlines.ONE:
            return content.rstrip("\n") + "\n"


def write_file(
    path: Path,
    content: str,
    *,
    trailing_newlines: TrailingNewlines = TrailingNewlines.PRESERVE,
) -> None:
    """Write content to file with optional newline normalisation.

    Args:
        path: The file path to write to.
        content: The content to write.
        trailing_newlines: The trailing newline normalisation mode.
    """
    content = normalise_trailing_newlines(content, trailing_newlines)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
