"""
Workspace data models.

These models describe the structure of the Kestrel workspace.
"""

from pathlib import Path

from pydantic import BaseModel, ConfigDict


class WorkspacePaths(BaseModel):
    """
    Represents every important directory inside the workspace.
    """

    model_config = ConfigDict(frozen=True)

    root: Path

    config: Path
    database: Path
    evidence: Path
    exports: Path
    logs: Path
    loot: Path
    projects: Path
    reports: Path
    screenshots: Path
    temp: Path

    def all_directories(self) -> list[Path]:
        """
        Return every managed directory.

        Returns
        -------
        list[Path]
            List of workspace directories.
        """

        return [
            self.root,
            self.config,
            self.database,
            self.evidence,
            self.exports,
            self.logs,
            self.loot,
            self.projects,
            self.reports,
            self.screenshots,
            self.temp,
        ]