import asyncio

from aiogram import Dispatcher

from src.entities.bot import bot
from src.entities.middlewares import register_middlewares
from src.routers.include_routers import include_routers


async def main():
    dp = Dispatcher()
    register_middlewares(dp)
    include_routers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
