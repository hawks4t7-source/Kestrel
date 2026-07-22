"""
Database engine factory.
"""

from __future__ import annotations

from pathlib import Path

from sqlalchemy import Engine, create_engine

from kestrel.config.manager import load_config


def create_database_engine() -> Engine:
    """
    Create and return the configured SQLAlchemy engine.
    """

    config = load_config()

    db_file = Path(config.workspace.directory).expanduser() / config.database.file

    database_url = f"sqlite:///{db_file}"

    engine = create_engine(
        database_url,
        echo=False,
        future=True,
    )

    return engine