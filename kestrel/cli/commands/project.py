"""
Project CLI commands.
"""

import typer
from rich.console import Console

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
    Create a new security assessment project.
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

    console.print(
        f"""
ID:
{project.id}

Name:
{project.name}

Status:
{project.status}
"""
    )

    session.close()