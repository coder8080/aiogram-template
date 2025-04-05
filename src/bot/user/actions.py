from sqlalchemy import select

from src.common.db import sessionmaker

from .models import User


async def get_or_create_user(chat_id: int, username: str):
    async with sessionmaker() as session:
        async with session.begin():
            query = await session.execute(
                select(User).where(User.id == chat_id)
            )
            row = query.scalar_one_or_none()

            if row:
                return

            user = User(id=chat_id, username=username)
            session.add(user)
