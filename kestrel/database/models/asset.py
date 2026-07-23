"""
Asset database model.

Stores discovered technical assets.
"""

from __future__ import annotations

import uuid

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from kestrel.database.models.base import Base
from kestrel.database.models.mixins import TimestampMixin


class Asset(Base, TimestampMixin):
    """
    Represents a discovered asset.
    """

    __tablename__ = "assets"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    target_id: Mapped[str] = mapped_column(
        ForeignKey("targets.id"),
        nullable=False,
    )

    asset_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="unknown",
    )

    value: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    technology: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    operating_system: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    target = relationship(
        "Target",
        back_populates="assets",
    )

    findings = relationship(
        "Finding",
        back_populates="asset",
        cascade="all, delete-orphan",
    )