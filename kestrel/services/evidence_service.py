"""
Evidence service.
"""

from sqlalchemy.orm import Session

from kestrel.database.models import Evidence


class EvidenceService:

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        finding_id: str,
        filename: str,
        file_path: str,
        evidence_type: str = "file",
        notes: str | None = None,
    ) -> Evidence:

        evidence = Evidence(
            finding_id=finding_id,
            filename=filename,
            file_path=file_path,
            evidence_type=evidence_type,
            notes=notes,
        )

        self.session.add(evidence)
        self.session.commit()
        self.session.refresh(evidence)

        return evidence

    def list(
        self,
        finding_id: str | None = None,
    ):

        query = self.session.query(Evidence)

        if finding_id:
            query = query.filter(
                Evidence.finding_id == finding_id
            )

        return query.all()

    def delete(
        self,
        evidence_id: str,
    ):

        evidence = (
            self.session.query(Evidence)
            .filter(
                Evidence.id == evidence_id
            )
            .first()
        )

        if evidence:
            self.session.delete(evidence)
            self.session.commit()

        return evidence