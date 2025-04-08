from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from src.common.environment import get_bool_env, get_int_env, get_str_env

USER = get_str_env("POSTGRES_USER")
PASSWORD = get_str_env("POSTGRES_PASSWORD")
HOST = get_str_env("POSTGRES_HOST")
PORT = get_int_env("POSTGRES_PORT")
DB = get_str_env("POSTGRES_DB")
LOCAL = get_bool_env("LOCAL")

db_url = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_async_engine(db_url, echo=LOCAL)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
