"""
Finding database model.

Stores discovered security vulnerabilities and observations.
"""

from __future__ import annotations

import uuid

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from kestrel.database.models.base import Base
from kestrel.database.models.mixins import TimestampMixin


class Finding(Base, TimestampMixin):
    """
    Represents a security finding.
    """

    __tablename__ = "findings"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    asset_id: Mapped[str] = mapped_column(
        ForeignKey("assets.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    severity: Mapped[str] = mapped_column(
        String(50),
        default="informational",
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="open",
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    impact: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    remediation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    asset = relationship(
        "Asset",
        back_populates="findings",
    )

    evidence = relationship(
        "Evidence",
        back_populates="finding",
        cascade="all, delete-orphan",
    )