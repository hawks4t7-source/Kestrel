"""
Project database model.

Represents a security assessment engagement.
"""

from __future__ import annotations

import uuid

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from kestrel.database.models.base import Base
from kestrel.database.models.mixins import TimestampMixin


class Project(Base, TimestampMixin):
    """
    Security assessment project.
    """

    __tablename__ = "projects"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="active",
        nullable=False,
    )

    targets = relationship(
        "Target",
        back_populates="project",
        cascade="all, delete-orphan",
    )