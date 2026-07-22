"""
Application lifecycle management.

Responsible for bootstrapping and shutting down the Kestrel
application.
"""

from __future__ import annotations

from loguru import logger

from kestrel.config.manager import load_config
from kestrel.workspace.manager import WorkspaceManager

from .application import KestrelApplication


class ApplicationLifecycle:
    """
    Handles startup and shutdown of the application.
    """

    def __init__(self, app: KestrelApplication) -> None:
        self.app = app

    def startup(self) -> None:
        """
        Initialize all core services.
        """

        logger.info("Starting Kestrel...")

        logger.info("Loading configuration...")
        config = load_config()

        logger.success("Configuration loaded.")

        logger.info("Initializing workspace...")
        workspace = WorkspaceManager()
        workspace.initialize()

        logger.success("Workspace initialized.")

        self.app.container.register("config", config)
        self.app.container.register("workspace", workspace)

        self.app.start()

        logger.success("Kestrel started successfully.")

    def shutdown(self) -> None:
        """
        Shutdown application.
        """

        logger.info("Stopping Kestrel...")

        self.app.shutdown()

        logger.success("Kestrel stopped.")