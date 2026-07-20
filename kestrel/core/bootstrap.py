"""
Kestrel Application Bootstrap

This module initializes all core services before the CLI starts.
"""

from kestrel.core.logger import logger

from kestrel.config.manager import load_config


def initialize() -> None:
    """
    Initialize the Kestrel application.
    """

    logger.info("======================================")
    logger.info("Starting Kestrel...")
    logger.info("Loading configuration...")

    config = load_config()

    logger.info("Configuration loaded successfully.")
    logger.info(f"Workspace: {config.workspace.directory}")
    logger.info(f"Database : {config.database.file}")
    logger.info("Bootstrap completed.")