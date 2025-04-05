from os import getenv

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

POSTGRES_USER = getenv("POSTGRES_USER")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
LOCAL = bool(getenv("LOCAL"))

assert POSTGRES_USER
assert POSTGRES_PASSWORD

db_url = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres:5432/bot"

engine = create_async_engine(db_url, echo=LOCAL)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
