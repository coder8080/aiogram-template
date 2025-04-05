import asyncio

from aiogram import Dispatcher

from src.bot.start.router import router as start_router
from src.bot.user.middlewares import GetUserMiddleware
from src.common.bot import bot


async def main():
    dp = Dispatcher()

    dp.update.middleware(GetUserMiddleware())
    dp.include_router(start_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
