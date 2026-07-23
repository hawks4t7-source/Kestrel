import typer

from rich.console import Console
from rich.table import Table

from kestrel.database.manager import DatabaseManager
from kestrel.services.asset_service import AssetService

asset_app = typer.Typer(
    help="Asset management commands."
)

console = Console()


@asset_app.command("add")
def add_asset(
    target_id: str = typer.Option(..., "--target"),
    hostname: str = typer.Option(..., "--hostname"),
    ip: str = typer.Option(..., "--ip"),
    os: str = typer.Option("", "--os"),
):

    db = DatabaseManager()
    db.initialize()

    session = db.session()

    service = AssetService(session)

    asset = service.create(
        target_id=target_id,
        hostname=hostname,
        ip_address=ip,
        operating_system=os,
    )

    console.print(
        "[green]✓ Asset added successfully[/green]"
    )

    console.print(asset.id)

    session.close()


@asset_app.command("list")
def list_assets(
    target_id: str = typer.Option(
        None,
        "--target",
    )
):

    db = DatabaseManager()
    db.initialize()

    session = db.session()

    service = AssetService(session)

    assets = service.list(target_id)

    table = Table(title="Assets")

    table.add_column("ID")
    table.add_column("Hostname")
    table.add_column("IP")
    table.add_column("OS")

    for asset in assets:

        table.add_row(
            asset.id,
            asset.hostname,
            asset.ip_address,
            asset.operating_system or "-",
        )

    console.print(table)

    session.close()


@asset_app.command("delete")
def delete_asset(
    asset_id: str = typer.Argument(...)
):

    db = DatabaseManager()
    db.initialize()

    session = db.session()

    service = AssetService(session)

    asset = service.delete(asset_id)

    if asset:
        console.print(
            "[green]✓ Asset deleted[/green]"
        )
    else:
        console.print(
            "[red]Asset not found[/red]"
        )

    session.close()