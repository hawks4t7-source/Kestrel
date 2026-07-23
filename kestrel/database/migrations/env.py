"""
Alembic migration environment.
"""

from logging.config import fileConfig

from sqlalchemy import create_engine

from alembic import context

from kestrel.config.manager import load_config
from kestrel.database.models import Base

# Import all models so SQLAlchemy metadata is populated
from kestrel.database.models.project import Project
from kestrel.database.models.target import Target
from kestrel.database.models.asset import Asset
from kestrel.database.models.finding import Finding
from kestrel.database.models.evidence import Evidence


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


settings = load_config()

config.set_main_option(
    "sqlalchemy.url",
    f"sqlite:///{settings.database.file}",
)


target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """
    Run migrations in offline mode.
    """

    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        render_as_batch=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Run migrations in online mode.
    """

    engine = create_engine(
        config.get_main_option("sqlalchemy.url")
    )

    with engine.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            render_as_batch=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()