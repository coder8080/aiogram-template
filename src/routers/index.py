from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.entities import TEXT

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(TEXT['start'])
