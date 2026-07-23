"""
Finding CLI commands.
"""

import typer

from rich.console import Console
from rich.table import Table

from kestrel.database.manager import DatabaseManager
from kestrel.services.finding_service import FindingService


finding_app = typer.Typer(
    help="Finding management commands."
)

console = Console()


@finding_app.command("add")
def add_finding(
    asset_id: str = typer.Option(
        ...,
        "--asset",
        "-a",
        help="Asset ID",
    ),
    title: str = typer.Option(
        ...,
        "--title",
        "-t",
        help="Finding title",
    ),
    severity: str = typer.Option(
        "medium",
        "--severity",
        "-s",
        help="Severity",
    ),
    cvss: float = typer.Option(
        None,
        "--cvss",
        help="CVSS score",
    ),
    description: str = typer.Option(
        None,
        "--description",
        help="Description",
    ),
    recommendation: str = typer.Option(
        None,
        "--recommendation",
        help="Recommendation",
    ),
):

    db = DatabaseManager()
    db.initialize()

    session = db.session()

    service = FindingService(session)

    finding = service.create(
        asset_id=asset_id,
        title=title,
        severity=severity,
        cvss_score=cvss,
        description=description,
        recommendation=recommendation,
    )

    console.print(
        "[green]✓ Finding added successfully[/green]"
    )

    console.print(f"""
ID:
{finding.id}

Title:
{finding.title}

Severity:
{finding.severity}

Status:
{finding.status}
""")

    session.close()


@finding_app.command("list")
def list_findings(
    asset_id: str = typer.Option(
        None,
        "--asset",
        "-a",
        help="Filter by Asset ID",
    )
):

    db = DatabaseManager()
    db.initialize()

    session = db.session()

    service = FindingService(session)

    findings = service.list(asset_id)

    table = Table(title="Kestrel Findings")

    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Severity")
    table.add_column("CVSS")
    table.add_column("Status")

    for finding in findings:

        table.add_row(
            finding.id,
            finding.title,
            finding.severity,
            str(finding.cvss_score),
            finding.status,
        )

    console.print(table)

    session.close()


@finding_app.command("delete")
def delete_finding(
    finding_id: str = typer.Argument(
        ...,
        help="Finding ID",
    )
):

    db = DatabaseManager()
    db.initialize()

    session = db.session()

    service = FindingService(session)

    finding = service.delete(
        finding_id
    )

    if finding:
        console.print(
            "[green]✓ Finding deleted[/green]"
        )
    else:
        console.print(
            "[red]Finding not found[/red]"
        )

    session.close()