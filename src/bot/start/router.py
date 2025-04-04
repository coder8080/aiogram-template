from aiogram.dispatcher.router import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from .lang import lang

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(lang["start"])
