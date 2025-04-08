import asyncio
from datetime import datetime

from sqlalchemy import create_engine

from src.common.environment import get_int_env, get_str_env

USER = get_str_env("POSTGRES_USER")
PASSWORD = get_str_env("POSTGRES_PASSWORD")
HOST = get_str_env("POSTGRES_HOST")
PORT = get_int_env("POSTGRES_PORT")
DB_TIMEOUT = get_int_env("DB_TIMEOUT")
DB = get_str_env("POSTGRES_DB")

db_url = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"


async def main():
    print("🏠 DB address:", db_url)
    print(
        f"⏱️ Waiting for db to be online. This may take up to \
{DB_TIMEOUT} seconds"
    )
    begin = datetime.now().timestamp()
    while True:
        seconds = datetime.now().timestamp() - begin
        if seconds > DB_TIMEOUT:
            raise Exception(f"Could not connect to db after {seconds} seconds")

        try:
            create_engine(db_url)
            break
        except Exception:
            await asyncio.sleep(0.1)

    print("✅ DB is online")


if __name__ == "__main__":
    asyncio.run(main())
