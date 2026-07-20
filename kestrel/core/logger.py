"""
Shared logger for the entire application.
"""

from loguru import logger

from kestrel.core.logging_config import configure_logging

configure_logging()

__all__ = ["logger"]