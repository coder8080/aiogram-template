from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from sqlalchemy.sql.sqltypes import BigInteger, String

from src.models.database import Base, sessionmaker


class User(Base):
    __tablename__ = "user_account"

    chat_id: Mapped[int] = mapped_column(
        BigInteger(), primary_key=True, index=True
    )
    username: Mapped[str] = mapped_column(String(64))
    blockers: Mapped[list["Blocker"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class Blocker(Base):
    __tablename__ = "blocker"

    message_id: Mapped[int] = mapped_column(
        BigInteger(), primary_key=True, index=True
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.chat_id"))

    user: Mapped["User"] = relationship(back_populates="blockers")


async def get_or_create_user(chat_id: int, username: str):
    async with sessionmaker() as session:
        async with session.begin():
            query = await session.execute(
                select(User).where(User.chat_id == chat_id)
            )
            row = query.first()
            if row is not None:
                return row[0]
            user = User(chat_id=chat_id, username=username)

            session.add(user)
            return user


async def add_blocker(chat_id: int, message_id: int):
    async with sessionmaker() as session:
        async with session.begin():
            query = await session.execute(
                select(User).where(User.chat_id == chat_id)
            )
            row = query.first()
            if row is None:
                raise Exception("User not found")

            user = row[0]

            blocker = Blocker(id=message_id, user=user)
            session.add(blocker)
