from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import TelegramObject


class GetUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        update: TelegramObject,
        data: Dict[str, Any],
    ):
        # chat_id, username = get_update_user_info(update)
        # if chat_id == 0:
        #     return await handler(update, data)

        # if not username:
        #     username = "unknown:" + str(chat_id)

        # query = User.select().where(User.chat_id == chat_id)
        # if not await query.aio_exists():
        #     user = await User.aio_create(chat_id=chat_id, username=username)
        #     data['user'] = user
        # else:
        #     user = await query.aio_first()
        #     data['user'] = user

        return await handler(update, data)


def register_middlewares(dp: Dispatcher):
    dp.message.middleware(GetUserMiddleware())
