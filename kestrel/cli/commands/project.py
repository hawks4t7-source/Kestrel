"""
Project CLI commands.
"""

import typer
from rich.console import Console
from rich.table import Table

from kestrel.database.manager import DatabaseManager
from kestrel.services.project_service import ProjectService

project_app = typer.Typer(
    help="Project management commands."
)

console = Console()


@project_app.command("create")
def create_project(
    name: str = typer.Option(
        ...,
        "--name",
        "-n",
        help="Project name",
    ),
    description: str = typer.Option(
        "",
        "--description",
        "-d",
        help="Project description",
    ),
):
    """
    Create a new project.
    """

    db = DatabaseManager()
    db.initialize()

    session = db.session()

    service = ProjectService(session)

    project = service.create(
        name=name,
        description=description,
    )

    console.print(
        "[green]✓ Project created successfully[/green]"
    )

    console.print(f"""
ID:
{project.id}

Name:
{project.name}

Status:
{project.status}
""")

    session.close()


@project_app.command("list")
def list_projects():
    """
    List all projects.
    """

    db = DatabaseManager()
    db.initialize()

    session = db.session()

    service = ProjectService(session)

    projects = service.list()

    table = Table(title="Kestrel Projects")

    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Status", style="yellow")
    table.add_column("Description", style="white")

    for project in projects:
        table.add_row(
            project.id,
            project.name,
            project.status,
            project.description or "-"
        )

    console.print(table)

    session.close()