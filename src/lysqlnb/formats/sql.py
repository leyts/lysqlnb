from typing import ClassVar

from lysqlnb.models import Cell, CellKind


class SQLFormat:
    """Handler for SQL file format."""

    suffix: ClassVar[str] = ".sql"

    def export_cell(self, cell: Cell) -> str:
        """Export a cell to SQL format.

        Markdown cells are converted to SQL comments with '-- ' prefix.
        Code cells are returned as-is.

        Args:
            cell: The cell to export.

        Returns:
            The cell content in SQL format.
        """
        if cell.kind == CellKind.MARKDOWN:
            return self._markdown_to_sql_comment(cell.value)
        return cell.value

    def _markdown_to_sql_comment(self, markdown: str) -> str:
        """Convert markdown content to SQL comments.

        Args:
            markdown: The markdown content to convert.

        Returns:
            The markdown content with each line prefixed by '-- '.
        """
        lines = markdown.splitlines()
        return "\n".join(f"-- {line}" for line in lines)
