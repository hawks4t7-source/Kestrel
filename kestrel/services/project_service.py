"""
Project service.
"""

from sqlalchemy.orm import Session

from kestrel.database.models import Project


class ProjectService:
    """
    Service for managing projects.
    """

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        name: str,
        description: str = "",
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

    def list(self) -> list[Project]:
        """
        Return all projects.
        """

        return (
            self.session.query(Project)
            .order_by(Project.created_at.desc())
            .all()
        )

    def get(
        self,
        project_id: str,
    ) -> Project | None:
        """
        Get a project by ID.
        """

        return (
            self.session.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

    def delete(
        self,
        project_id: str,
    ) -> bool:
        """
        Delete a project.
        """

        project = self.get(project_id)

        if not project:
            return False

        self.session.delete(project)
        self.session.commit()

        return True