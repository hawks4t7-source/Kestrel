"""
Database exception hierarchy.
"""

from __future__ import annotations


class DatabaseError(Exception):
    """Base database exception."""


class DatabaseConnectionError(DatabaseError):
    """Raised when a database connection cannot be established."""


class DatabaseInitializationError(DatabaseError):
    """Raised when database initialization fails."""


class DatabaseSessionError(DatabaseError):
    """Raised when session creation or management fails."""