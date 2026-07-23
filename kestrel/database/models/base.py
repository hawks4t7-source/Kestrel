"""
SQLAlchemy declarative base configuration.

All Kestrel database models inherit from this base.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all ORM models.
    """

    pass