"""
Target CLI commands.
"""

import typer

from rich.console import Console
from rich.table import Table

from kestrel.database.manager import DatabaseManager
from kestrel.database.models import Target
from kestrel.services.target_service import TargetService


target_app = typer.Typer(
    help="Target management commands."
)

console = Console()


@target_app.command("add")
def add_target(
    project_id: str = typer.Option(
        ...,
        "--project",
        "-p",
        help="Project ID"
    ),

    name: str = typer.Option(
        ...,
        "--name",
        "-n",
        help="Target name"
    ),

    value: str = typer.Option(
        ...,
        "--value",
        "-v",
        help="Target value"
    ),

    target_type: str = typer.Option(
        "domain",
        "--type",
        "-t",
        help="Target type"
    ),

):

    db = DatabaseManager()
    db.initialize()

    session = db.session()

    try:

        service = TargetService(
            session
        )

        target = service.create(
            project_id=project_id,
            name=name,
            value=value,
            target_type=target_type,
        )


        console.print(
            "[green]✓ Target added successfully[/green]"
        )

        console.print(
            f"""
ID:
{target.id}

Name:
{target.name}

Value:
{target.value}

Type:
{target.target_type}
"""
        )

    finally:
        session.close()



@target_app.command("list")
def list_targets(
    project_id: str = typer.Option(
        None,
        "--project",
        "-p",
        help="Filter targets by project ID"
    )
):
    """
    List available targets.
    """

    db = DatabaseManager()
    db.initialize()

    session = db.session()

    try:

        query = session.query(Target)

        if project_id:
            query = query.filter(
                Target.project_id == project_id
            )


        targets = query.all()


        if not targets:
            console.print(
                "[yellow]No targets found.[/yellow]"
            )
            return


        table = Table(
            title="Kestrel Targets"
        )


        table.add_column(
            "ID",
            style="cyan"
        )

        table.add_column(
            "Name"
        )

        table.add_column(
            "Value"
        )

        table.add_column(
            "Type"
        )


        for target in targets:

            table.add_row(
                str(target.id),
                target.name,
                target.value,
                target.target_type,
            )


        console.print(table)


    finally:
        session.close()