"""
Finding service.
"""

from sqlalchemy.orm import Session

from kestrel.database.models import Finding


class FindingService:
    """
    Service for managing findings.
    """

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        asset_id: str,
        title: str,
        severity: str,
        cvss_score: float | None = None,
        description: str | None = None,
        recommendation: str | None = None,
    ) -> Finding:

        finding = Finding(
            asset_id=asset_id,
            title=title,
            severity=severity,
            cvss_score=cvss_score,
            description=description,
            recommendation=recommendation,
        )

        self.session.add(finding)
        self.session.commit()
        self.session.refresh(finding)

        return finding

    def list(
        self,
        asset_id: str | None = None,
    ):

        query = self.session.query(Finding)

        if asset_id:
            query = query.filter(
                Finding.asset_id == asset_id
            )

        return query.all()

    def get(
        self,
        finding_id: str,
    ) -> Finding | None:

        return (
            self.session.query(Finding)
            .filter(
                Finding.id == finding_id
            )
            .first()
        )

    def update(
        self,
        finding_id: str,
        **kwargs,
    ) -> Finding | None:

        finding = self.get(finding_id)

        if not finding:
            return None

        for key, value in kwargs.items():
            if value is not None and hasattr(finding, key):
                setattr(finding, key, value)

        self.session.commit()
        self.session.refresh(finding)

        return finding

    def delete(
        self,
        finding_id: str,
    ) -> Finding | None:

        finding = self.get(finding_id)

        if not finding:
            return None

        self.session.delete(finding)
        self.session.commit()

        return finding