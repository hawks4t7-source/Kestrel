"""
Target database model.

Represents an assessment target.
"""

from __future__ import annotations

import uuid

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from kestrel.database.models.base import Base
from kestrel.database.models.mixins import TimestampMixin


class Target(Base, TimestampMixin):
    """
    Represents a target inside a project.
    """

    __tablename__ = "targets"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    project_id: Mapped[str] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    target_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="unknown",
    )

    value: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    project = relationship(
        "Project",
        back_populates="targets",
    )

    assets = relationship(
        "Asset",
        back_populates="target",
        cascade="all, delete-orphan",
    )