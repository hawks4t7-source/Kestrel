"""
kestrel.workspace.manager
~~~~~~~~~~~~~~~~~~~~~~~~~

Workspace Manager.

Responsible for:

- Initializing the workspace
- Creating required directories
- Validating workspace structure
- Returning workspace information

The Workspace Manager never stores application data.
It only manages the filesystem layout.

Author:
    Kestrel Development Team
"""

from __future__ import annotations

from pathlib import Path

from loguru import logger

from kestrel.workspace.exceptions import (
    DirectoryCreationError,
    WorkspaceValidationError,
)
from kestrel.workspace.models import WorkspacePaths
from kestrel.workspace.paths import WorkspacePathsBuilder


class WorkspaceManager:
    """
    Manages the Kestrel workspace.

    This class is the single source of truth for all
    workspace filesystem operations.
    """

    def __init__(self) -> None:
        self._builder = WorkspacePathsBuilder()
        self._paths = self._builder.build()

    @property
    def paths(self) -> WorkspacePaths:
        """
        Return the workspace paths model.
        """
        return self._paths

    @property
    def root(self) -> Path:
        """
        Return the workspace root.
        """
        return self._paths.root

    def initialize(self) -> WorkspacePaths:
        """
        Create the complete workspace if required.

        Returns
        -------
        WorkspacePaths
        """

        logger.info("Initializing workspace...")

        for directory in self._paths.all_directories():
            try:
                directory.mkdir(parents=True, exist_ok=True)
            except OSError as exc:
                logger.exception(
                    "Failed creating directory: {}",
                    directory,
                )
                raise DirectoryCreationError(
                    f"Unable to create directory: {directory}"
                ) from exc

        logger.success("Workspace initialized.")

        return self._paths

    def validate(self) -> bool:
        """
        Verify every required directory exists.

        Raises
        ------
        WorkspaceValidationError

        Returns
        -------
        bool
        """

        missing: list[Path] = []

        for directory in self._paths.all_directories():
            if not directory.exists():
                missing.append(directory)

        if missing:
            raise WorkspaceValidationError(
                "Missing directories:\n"
                + "\n".join(str(item) for item in missing)
            )

        return True

    def exists(self) -> bool:
        """
        Check whether the workspace root exists.
        """

        return self.root.exists()

    def info(self) -> dict[str, str]:
        """
        Return workspace information.
        """

        return {
            "root": str(self._paths.root),
            "projects": str(self._paths.projects),
            "reports": str(self._paths.reports),
            "database": str(self._paths.database),
            "logs": str(self._paths.logs),
            "evidence": str(self._paths.evidence),
            "loot": str(self._paths.loot),
            "exports": str(self._paths.exports),
            "screenshots": str(self._paths.screenshots),
            "temp": str(self._paths.temp),
        }