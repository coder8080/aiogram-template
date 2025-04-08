from aiogram import Bot

from common.environment import get_str_env

TOKEN = get_str_env("TOKEN")

assert TOKEN

bot = Bot(TOKEN)
