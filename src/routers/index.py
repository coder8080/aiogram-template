from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start(message: Message, chat_id: int, username: str):
    await message.answer(f"hello {chat_id} {username}")
