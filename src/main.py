import asyncio

from aiogram import Dispatcher

from src.entities import bot
from src.routers import include_routers


async def main():
    dp = Dispatcher()
    # register_middlewares(dp)
    include_routers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
