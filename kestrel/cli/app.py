"""
Main command-line interface for Kestrel.
"""

import typer
from rich.console import Console
from rich.panel import Panel

from kestrel import __version__
from kestrel.cli.commands.project import project_app
from kestrel.cli.commands.target import target_app
from kestrel.cli.commands.asset import asset_app

app = typer.Typer(
    help="AI-powered security assessment platform."
)

console = Console()
app.add_typer(
    project_app,
    name="project"
)

app.add_typer(
    target_app,
    name="target"
)
app.add_typer(
    asset_app,
    name="asset",
)

@app.callback(invoke_without_command=True)
def main() -> None:
    """
    Display the welcome banner.
    """
    console.print(
        Panel.fit(
            f"[bold cyan]Kestrel[/bold cyan]\n"
            f"Version: {__version__}\n"
            "Professional Security Assessment Platform",
            title="Welcome",
        )
    )


@app.command()
def version() -> None:
    """
    Display the application version.
    """
    console.print(f"Kestrel Version: [green]{__version__}[/green]")


@app.command()
def doctor() -> None:
    """
    Perform a basic environment check.
    """
    console.print("[green]✓[/green] CLI loaded successfully.")

    