"""finding_management

Revision ID: a50a3eeafc61
Revises: 8b103749517c
Create Date: 2026-07-24 03:35:13.043071
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "a50a3eeafc61"
down_revision: Union[str, Sequence[str], None] = "8b103749517c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    with op.batch_alter_table("findings") as batch_op:

        batch_op.add_column(
            sa.Column("cvss_score", sa.Float(), nullable=True)
        )

        batch_op.add_column(
            sa.Column("recommendation", sa.Text(), nullable=True)
        )

        batch_op.alter_column(
            "severity",
            existing_type=sa.String(length=50),
            type_=sa.String(length=20),
            existing_nullable=False,
        )

        batch_op.alter_column(
            "status",
            existing_type=sa.String(length=50),
            type_=sa.String(length=30),
            existing_nullable=False,
        )

        batch_op.drop_column("impact")
        batch_op.drop_column("remediation")


def downgrade() -> None:
    """Downgrade schema."""

    with op.batch_alter_table("findings") as batch_op:

        batch_op.add_column(
            sa.Column("remediation", sa.Text(), nullable=True)
        )

        batch_op.add_column(
            sa.Column("impact", sa.Text(), nullable=True)
        )

        batch_op.alter_column(
            "status",
            existing_type=sa.String(length=30),
            type_=sa.String(length=50),
            existing_nullable=False,
        )

        batch_op.alter_column(
            "severity",
            existing_type=sa.String(length=20),
            type_=sa.String(length=50),
            existing_nullable=False,
        )

        batch_op.drop_column("recommendation")
        batch_op.drop_column("cvss_score")