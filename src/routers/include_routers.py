from aiogram import Dispatcher

from src.routers.index import router as index_router


def include_routers(dp: Dispatcher):
    dp.include_router(index_router)
