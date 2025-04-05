from aiogram.dispatcher.router import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import User as TgUser

from .lang import lang

router = Router()


@router.message(CommandStart())
async def start(message: Message, actor: TgUser):
    await message.answer(lang("start", actor))
