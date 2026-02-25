import logging
from typing import TYPE_CHECKING

from lysqlnb.formats import MarkdownFormat, SQLFormat
from lysqlnb.io import write_file
from lysqlnb.models import CellKind, Notebook, TrailingNewlines

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)

_sql_format = SQLFormat()
_markdown_format = MarkdownFormat()


def export_notebook(
    notebook: Notebook,
    output_path: Path,
    *,
    include_markdown: bool = True,
    split_cells: bool = False,
    trailing_newlines: TrailingNewlines = TrailingNewlines.PRESERVE,
) -> list[Path]:
    """Export a notebook.

    Args:
        notebook: The notebook to export.
        output_path: The output file or directory path.
        include_markdown: Whether to include markdown cells.
        split_cells: Whether to split cells into separate files.
        trailing_newlines: The trailing newline normalisation mode.

    Returns:
        A list of created file paths.
    """
    if split_cells:
        return _export_split(
            notebook,
            output_path,
            include_markdown=include_markdown,
            trailing_newlines=trailing_newlines,
        )
    return _export_single(
        notebook,
        output_path,
        include_markdown=include_markdown,
        trailing_newlines=trailing_newlines,
    )


def _export_single(
    notebook: Notebook,
    output_path: Path,
    *,
    include_markdown: bool,
    trailing_newlines: TrailingNewlines,
) -> list[Path]:
    """Export all cells to a single SQL file.

    Args:
        notebook: The notebook to export.
        output_path: The output file path.
        include_markdown: Whether to include markdown cells as SQL comments.
        trailing_newlines: The trailing newline normalisation mode.

    Returns:
        A list containing the output file path.
    """
    sections: list[str] = []

    for cell in notebook.cells:
        if cell.kind == CellKind.MARKDOWN:
            if include_markdown:
                sections.append(_sql_format.export_cell(cell))
        else:
            sections.append(_sql_format.export_cell(cell))

    content = "\n\n".join(sections)

    if not content.strip():
        logger.warning("Export produced empty output")

    write_file(output_path, content, trailing_newlines=trailing_newlines)
    return [output_path]


def _export_split(
    notebook: Notebook,
    output_dir: Path,
    *,
    include_markdown: bool,
    trailing_newlines: TrailingNewlines,
) -> list[Path]:
    """Export each cell to a separate file.

    Args:
        notebook: The notebook to export.
        output_dir: The output directory path.
        include_markdown: Whether to include markdown cells.
        trailing_newlines: The trailing newline normalisation mode.

    Returns:
        A list of created file paths.
    """
    created_files: list[Path] = []
    cell_number = 1

    for cell in notebook.cells:
        if cell.kind == CellKind.MARKDOWN:
            if not include_markdown:
                continue
            fmt = _markdown_format
        else:
            fmt = _sql_format

        content = fmt.export_cell(cell)
        file_path = output_dir / f"{cell_number:03d}{fmt.suffix}"

        write_file(file_path, content, trailing_newlines=trailing_newlines)

        created_files.append(file_path)
        cell_number += 1

    if not created_files:
        logger.warning("Export produced no files")

    return created_files
