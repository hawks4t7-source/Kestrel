"""
Project service.

Handles project creation and management.
"""

from sqlalchemy.orm import Session

from kestrel.database.models import Project


class ProjectService:
    """
    Service layer for projects.
    """

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        name: str,
        description: str | None = None,
    ) -> Project:
        """
        Create a new project.
        """

        project = Project(
            name=name,
            description=description,
        )

        self.session.add(project)
        self.session.commit()
        self.session.refresh(project)

        return project