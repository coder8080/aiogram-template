from src.entities.bot import bot
from src.entities.constants import (
    LOCAL,
    POSTGRES_PASSWORD,
    POSTGRES_USER,
    TEXT,
)

from .middlewares import register_middlewares

__all__ = ["TEXT", "register_middlewares", "bot", "POSTGRES_USER",
    "POSTGRES_PASSWORD", "LOCAL"]
