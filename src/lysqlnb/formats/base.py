from typing import TYPE_CHECKING, ClassVar, Protocol

if TYPE_CHECKING:
    from lysqlnb.models import Cell


class FormatProtocol(Protocol):
    """Protocol defining the interface for format handlers."""

    suffix: ClassVar[str]
    """File extension for this format."""

    def export_cell(self, cell: Cell) -> str:
        """Export a single cell to this format.

        Args:
            cell: The cell to export.

        Returns:
            The cell content in this format.
        """
        ...
