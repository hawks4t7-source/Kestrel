from logging.config import fileConfig

from sqlalchemy import create_engine
from alembic import context

from kestrel.config.manager import load_config
from kestrel.database.models import Base

# Import all models
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
    f"sqlite:///{settings.database.file}"
)

target_metadata = Base.metadata


def run_migrations_offline():
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():

    engine = create_engine(
        config.get_main_option("sqlalchemy.url")
    )

    with engine.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()