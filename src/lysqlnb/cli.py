import logging

from cyclopts import App, Group, Parameter
from rich.console import Console
from rich.logging import RichHandler

from lysqlnb.commands import export

logging.basicConfig(
    level=logging.WARNING,
    format="%(message)s",
    handlers=[RichHandler(console=Console(stderr=True), show_time=False)],
)

GlobalGroup = Group(name="Global Options")

app = App(
    name="oracle-sql-notebooks",
    help="Parse and export Oracle SQL notebooks.",
    default_parameter=Parameter(negative=()),
    version_flags=["-V", "--version"],
    help_flags=["-h", "--help", "help"],
)
app["--help"].group = GlobalGroup
app["--version"].group = GlobalGroup

app.command(export)
