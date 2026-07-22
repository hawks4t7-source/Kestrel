"""
Database session management.
"""

from __future__ import annotations

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine


def create_session_factory(engine: Engine) -> sessionmaker:
    """
    Create a SQLAlchemy session factory.
    """

    return sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
    )


def create_session(factory: sessionmaker) -> Session:
    """
    Create a new database session.
    """

    return factory()