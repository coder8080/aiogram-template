import asyncio

from aiogram import Dispatcher
from aiohttp import ClientSession

from common.environment import get_str_env
from src.bot.start.router import router as start_router
from src.bot.user.middlewares import GetUserMiddleware
from src.common.bot import bot
from src.server import start_site


async def main():
    dp = Dispatcher()

    dp.update.middleware(GetUserMiddleware())
    dp.include_router(start_router)

    await start_site()

    session = ClientSession()

    POD_NAME = get_str_env("POD_NAME")

    print("⏱️ Waiting to become main instance...")

    while True:
        try:
            response = await session.get("http://bot-podname/pod_name")
            json = await response.json()
            assert json["pod_name"] == POD_NAME
            await asyncio.sleep(0.05)
            break
        except Exception:
            pass

    print("✅ Pod has become main instance. Starting polling")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
