"""
Bootstrap exceptions for Kestrel.

Defines the exception hierarchy used during application startup
and shutdown.
"""

from __future__ import annotations


class BootstrapError(Exception):
    """
    Base exception for all bootstrap-related errors.
    """


class StartupError(BootstrapError):
    """
    Raised when Kestrel fails during startup.
    """


class ShutdownError(BootstrapError):
    """
    Raised when Kestrel fails during shutdown.
    """