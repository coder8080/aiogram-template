from typing import Any, Awaitable, Callable, Dict, cast

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update
from aiogram.types import User as TgUser

from .actions import get_or_create_user


def get_update_user_info(update: Update):
    actor: TgUser | None = None

    if update.message and update.message.from_user:
        actor = update.message.from_user
    elif update.callback_query and update.callback_query.from_user:
        actor = update.callback_query.from_user
    elif update.pre_checkout_query and update.pre_checkout_query.from_user:
        actor = update.pre_checkout_query.from_user

    if actor and actor.username is None:
        actor.username = f"unknown:${actor.id}"

    return actor


class GetUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        _update: TelegramObject,
        data: Dict[str, Any],
    ):
        update = cast(Update, _update)
        actor = get_update_user_info(update)
        if actor is None:
            return await handler(update, data)

        await get_or_create_user(actor.id, actor.username or "unknown")

        data["actor"] = actor

        return await handler(update, data)
