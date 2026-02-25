from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from lysqlnb.models import Cell


class MarkdownFormat:
    """Handler for Markdown file format."""

    suffix: ClassVar[str] = ".md"

    def export_cell(self, cell: Cell) -> str:
        """Export a cell to Markdown format.

        Args:
            cell: The cell to export.

        Returns:
            The cell content (passthrough).
        """
        return cell.value
