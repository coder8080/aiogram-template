from os import getenv

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

POSTGRES_USER = getenv("POSTGRES_USER")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
POSTGRES_URL = getenv("POSTGRES_URL")
POSTGRES_DB = getenv("POSTGRES_DB")
LOCAL = bool(getenv("LOCAL"))

assert POSTGRES_USER
assert POSTGRES_PASSWORD
assert POSTGRES_URL
assert POSTGRES_DB

db_url = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_URL}/{POSTGRES_DB}"

engine = create_async_engine(db_url, echo=LOCAL)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
