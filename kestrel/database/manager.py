"""
Database manager.

Handles database initialization,
engine creation and session access.
"""

from __future__ import annotations

from sqlalchemy import inspect, create_engine
from sqlalchemy.orm import sessionmaker, Session

from kestrel.core.logger import logger
from kestrel.config.manager import load_config

from kestrel.database.models import (
    Base,
    Project,
    Target,
    Asset,
    Finding,
    Evidence,
)


class DatabaseManager:
    """
    Manages SQLAlchemy database lifecycle.
    """

    def __init__(self) -> None:
        self.engine = None
        self.SessionLocal = None

    def initialize(self) -> None:
        """
        Initialize database engine
        and create tables.
        """

        logger.info("Initializing database...")

        config = load_config()

        database_url = (
            f"sqlite:///{config.database.file}"
        )

        self.engine = create_engine(
            database_url,
            echo=False,
        )

        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
        )

         # Register models
        # Importing models ensures SQLAlchemy
        # knows all metadata
        _ = (
            Project,
            Target,
            Asset,
            Finding,
            Evidence,
        )

        # Database schema is managed by Alembic.

        logger.success(
            "Database initialized."
        )

    def session(self) -> Session:
        """
        Create a new database session.
        """

        if self.SessionLocal is None:
            raise RuntimeError(
                "Database is not initialized."
            )

        return self.SessionLocal()

    def tables(self) -> list[str]:
        """
        Return available database tables.
        """

        if self.engine is None:
            raise RuntimeError(
                "Database is not initialized."
            )

        inspector = inspect(
            self.engine
        )

        return inspector.get_table_names()