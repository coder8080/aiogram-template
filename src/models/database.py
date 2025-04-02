from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from src.entities import LOCAL, POSTGRES_PASSWORD, POSTGRES_USER


class Base(AsyncAttrs, DeclarativeBase):
    pass


DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres:5432/bot"

engine = create_async_engine(DATABASE_URL, echo=LOCAL)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
