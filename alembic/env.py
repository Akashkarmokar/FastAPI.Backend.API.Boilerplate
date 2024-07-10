import asyncio
import os
from logging.config import fileConfig

from alembic import context

from api.core.db import async_engine

# Must Import All Of your Models here
# from api.models.Register import Register
# from api.models.Profile import Profile
# from api.models.SocialMedia import SocialMedia
from api.models.Bio import Bio

from api.models.Base import Base



# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# here we allow ourselves to pass interpolation vars to alembic.ini
# fron the host env
section = config.config_ini_section
config.set_section_option(section, "DB_USER", os.environ.get("DB_USER"))
config.set_section_option(section, "DB_PASSWORD", os.environ.get("DB_PASSWORD"))
config.set_section_option(section,"DB_HOST", os.environ.get("DB_HOST"))
config.set_section_option(section,"DB_PORT", os.environ.get("DB_PORT"))
config.set_section_option(section,"DB_NAME", os.environ.get("DB_NAME"))

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def include_object(obj, name, type_, reflected, compare_to):
    if obj.info.get("skip_autogen", False):
        return False

    return True


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = async_engine

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


asyncio.run(run_migrations_online())
# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     asyncio.run(run_migrations_online())
