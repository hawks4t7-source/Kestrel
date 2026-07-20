"""
kestrel.workspace.paths
~~~~~~~~~~~~~~~~~~~~~~~

Workspace path utilities.

This module centralizes every filesystem path used by Kestrel.

Nothing in the application should manually construct workspace
paths using string concatenation.

Always use WorkspacePathsBuilder.

Author:
    Kestrel Development Team
"""

from __future__ import annotations

from pathlib import Path

from kestrel.config.manager import load_config
from kestrel.workspace.models import WorkspacePaths


class WorkspacePathsBuilder:
    """
    Builds every directory used by the Kestrel workspace.

    The builder does not create directories.
    It only resolves and returns paths.

    Directory creation is the responsibility of
    WorkspaceManager.
    """

    def __init__(self) -> None:
        self.config = load_config()

    @property
    def root(self) -> Path:
        """
        Return workspace root directory.
        """

        return Path(self.config.workspace.directory).expanduser().resolve()

    def build(self) -> WorkspacePaths:
        """
        Build and return every workspace path.

        Returns
        -------
        WorkspacePaths
        """

        root = self.root

        return WorkspacePaths(
            root=root,
            config=root / "config",
            database=root / "database",
            evidence=root / "evidence",
            exports=root / "exports",
            logs=root / "logs",
            loot=root / "loot",
            projects=root / "projects",
            reports=root / "reports",
            screenshots=root / "screenshots",
            temp=root / "temp",
        )