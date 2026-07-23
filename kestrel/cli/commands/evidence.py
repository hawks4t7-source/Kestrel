"""
Evidence CLI commands.
"""

import typer

from rich.console import Console
from rich.table import Table

from kestrel.database.manager import DatabaseManager
from kestrel.services.evidence_service import EvidenceService

evidence_app = typer.Typer(
    help="Evidence management commands."
)

console = Console()


@evidence_app.command("add")
def add_evidence(
    finding_id: str = typer.Option(
        ...,
        "--finding",
        "-f",
        help="Finding ID",
    ),
    filename: str = typer.Option(
        ...,
        "--filename",
        help="Evidence filename",
    ),
    file_path: str = typer.Option(
        ...,
        "--path",
        help="Path to evidence file",
    ),
    evidence_type: str = typer.Option(
        "file",
        "--type",
        help="Evidence type",
    ),
    notes: str = typer.Option(
        "",
        "--notes",
        help="Evidence notes",
    ),
):

    db = DatabaseManager()
    db.initialize()

    session = db.session()

    service = EvidenceService(session)

    evidence = service.create(
        finding_id=finding_id,
        filename=filename,
        file_path=file_path,
        evidence_type=evidence_type,
        notes=notes,
    )

    console.print(
        "[green]✓ Evidence added successfully[/green]"
    )

    console.print(f"""
ID:
{evidence.id}

Filename:
{evidence.filename}

Type:
{evidence.evidence_type}
""")

    session.close()


@evidence_app.command("list")
def list_evidence(
    finding_id: str = typer.Option(
        None,
        "--finding",
        "-f",
        help="Filter by Finding ID",
    ),
):

    db = DatabaseManager()
    db.initialize()

    session = db.session()

    service = EvidenceService(session)

    evidence_items = service.list(
        finding_id=finding_id
    )

    table = Table(title="Kestrel Evidence")

    table.add_column("ID")
    table.add_column("Filename")
    table.add_column("Type")
    table.add_column("Path")

    for evidence in evidence_items:

        table.add_row(
            evidence.id,
            evidence.filename,
            evidence.evidence_type,
            evidence.file_path,
        )

    console.print(table)

    session.close()


@evidence_app.command("delete")
def delete_evidence(

    evidence_id: str = typer.Argument(
        ...,
        help="Evidence ID",
    ),
):

    db = DatabaseManager()
    db.initialize()

    session = db.session()

    service = EvidenceService(session)

    evidence = service.delete(
        evidence_id
    )

    if evidence:

        console.print(
            "[green]✓ Evidence deleted successfully[/green]"
        )

    else:

        console.print(
            "[red]Evidence not found.[/red]"
        )

    session.close()