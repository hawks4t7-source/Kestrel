"""
Evidence database model.

Stores evidence attached to findings.
"""

from __future__ import annotations

import uuid

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from kestrel.database.models.base import Base
from kestrel.database.models.mixins import TimestampMixin


class Evidence(Base, TimestampMixin):
    """
    Evidence attached to a finding.
    """

    __tablename__ = "evidence"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    finding_id: Mapped[str] = mapped_column(
        ForeignKey("findings.id"),
        nullable=False,
    )

    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    evidence_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="file",
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    finding = relationship(
        "Finding",
        back_populates="evidence",
    )