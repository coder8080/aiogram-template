from typing import Any, Awaitable, Callable, Dict, cast

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update

from .actions import get_or_create_user


def get_update_user_info(update: Update):
    chat_id: int = 0
    username: str | None = None

    if update.message and update.message.from_user:
        chat_id = update.message.from_user.id
        username = update.message.from_user.username
    elif update.callback_query and update.callback_query.from_user:
        chat_id = update.callback_query.from_user.id
        username = update.callback_query.from_user.username
    elif update.pre_checkout_query and update.pre_checkout_query.from_user:
        chat_id = update.pre_checkout_query.from_user.id
        username = update.pre_checkout_query.from_user.username

    if username is None:
        username = f"unknown:${chat_id}"

    return chat_id, username


class GetUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        _update: TelegramObject,
        data: Dict[str, Any],
    ):
        update = cast(Update, _update)
        chat_id, username = get_update_user_info(update)
        if chat_id == 0:
            return await handler(update, data)

        await get_or_create_user(chat_id, username)

        data["chat_id"] = chat_id
        data["username"] = username

        return await handler(update, data)
