"""
Target service.

Handles target creation and management.
"""

from sqlalchemy.orm import Session

from kestrel.database.models import Target, Project


class TargetService:
    """
    Service layer for targets.
    """

    def __init__(self, session: Session):
        self.session = session


    def create(
        self,
        project_id: str,
        name: str,
        value: str,
        target_type: str,
        description: str | None = None,
    ) -> Target:
        """
        Create a target.
        """

        project = (
            self.session
            .query(Project)
            .filter(
                Project.id == project_id
            )
            .first()
        )

        if not project:
            raise ValueError(
                "Project not found."
            )


        target = Target(
            project_id=project_id,
            name=name,
            value=value,
            target_type=target_type,
            description=description,
        )


        self.session.add(target)
        self.session.commit()
        self.session.refresh(target)

        return target