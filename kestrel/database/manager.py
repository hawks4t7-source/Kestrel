"""
Database manager.
"""

from __future__ import annotations

from loguru import logger
from sqlalchemy.orm import Session

from .base import Base
from .engine import create_database_engine
from .session import create_session
from .session import create_session_factory


class DatabaseManager:
    """
    Central database manager.
    """

    def __init__(self) -> None:

        self.engine = create_database_engine()

        self.session_factory = create_session_factory(
            self.engine
        )

    def initialize(self) -> None:

        logger.info("Initializing database...")

        Base.metadata.create_all(self.engine)

        logger.success("Database initialized.")

    def session(self) -> Session:

        return create_session(
            self.session_factory
        )