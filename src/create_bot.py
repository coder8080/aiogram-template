from os import getenv

from aiogram import Bot

TOKEN = getenv("TOKEN")

assert TOKEN

bot = Bot(TOKEN)
