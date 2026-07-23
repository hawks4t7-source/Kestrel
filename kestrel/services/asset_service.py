"""
Asset service.
"""

from sqlalchemy.orm import Session

from kestrel.database.models import Asset


class AssetService:

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        target_id: str,
        hostname: str,
        ip_address: str,
        operating_system: str | None = None,
    ) -> Asset:

        asset = Asset(
            target_id=target_id,
            hostname=hostname,
            ip_address=ip_address,
            operating_system=operating_system,
        )

        self.session.add(asset)
        self.session.commit()
        self.session.refresh(asset)

        return asset

    def list(
        self,
        target_id: str | None = None,
    ):

        query = self.session.query(Asset)

        if target_id:
            query = query.filter(
                Asset.target_id == target_id
            )

        return query.all()

    def delete(
        self,
        asset_id: str,
    ):

        asset = (
            self.session.query(Asset)
            .filter(
                Asset.id == asset_id
            )
            .first()
        )

        if asset:

            self.session.delete(asset)
            self.session.commit()

        return asset