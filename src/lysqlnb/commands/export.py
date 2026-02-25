from pathlib import Path  # noqa: TC003
from typing import Annotated

from cyclopts import Parameter
from cyclopts.types import ResolvedExistingPath  # noqa: TC002
from rich.console import Console

from lysqlnb.core import export_notebook
from lysqlnb.models import TrailingNewlines
from lysqlnb.parser import NotebookParseError, parse_notebook

console = Console()


def export(
    input_file: Annotated[ResolvedExistingPath, Parameter(alias="-i")],
    output: Annotated[Path | None, Parameter(name=["--output", "-o"])] = None,
    *,
    include_markdown: Annotated[
        bool,
        Parameter(negative="--no-include-markdown"),
    ] = True,
    split: Annotated[bool, Parameter(negative="--no-split")] = False,
    trailing_newlines: TrailingNewlines = TrailingNewlines.PRESERVE,
) -> None:
    """Export a .sqlnb notebook.

    Args:
        input_file:
            Path to the .sqlnb file
        output:
            Output path (file or directory for --split)
        include_markdown:
            Include markdown cells as SQL comments
        split:
            Export each cell as a separate file
        trailing_newlines:
            Trailing newline handling: 'preserve' keeps original,
            'none' removes all, 'one' ensures exactly one
    """
    # if --split, file cannot exist but directory can
    # if not --split, directory cannot exist but file can
    # how to handle overwrites? --force/--overwrite flag?

    try:
        notebook = parse_notebook(input_file)
    except NotebookParseError as e:
        console.print(f"[red]Error:[/red] {e}")
        raise SystemExit(1) from e

    if output is None:
        if split:
            output = input_file.with_suffix("")
        else:
            output = input_file.with_suffix(".sql")

    created_files = export_notebook(
        notebook,
        output,
        include_markdown=include_markdown,
        split_cells=split,
        trailing_newlines=trailing_newlines,
    )

    for file_path in created_files:
        console.print(f"[green]Created:[/green] {file_path}")
