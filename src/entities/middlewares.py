from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import (
    CallbackQuery,
    Message,
    PreCheckoutQuery,
    TelegramObject,
)

from src.models.user import get_or_create_user


def get_update_user_info(update: TelegramObject):
    chat_id: int = 0
    username: str | None = None
    if (
        isinstance(update, Message) or isinstance(update, PreCheckoutQuery)
    ) and update.from_user:
        chat_id = update.from_user.id
        username = update.from_user.username
    elif isinstance(update, CallbackQuery):
        chat_id = update.from_user.id
        username = update.from_user.username

    if username is None:
        username = f"unknown:${chat_id}"

    return chat_id, username


class GetUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        update: TelegramObject,
        data: Dict[str, Any],
    ):
        chat_id, username = get_update_user_info(update)
        if chat_id == 0:
            return await handler(update, data)

        await get_or_create_user(chat_id, username)

        data["chat_id"] = chat_id
        data["username"] = username

        return await handler(update, data)


def register_middlewares(dp: Dispatcher):
    dp.message.middleware(GetUserMiddleware())
