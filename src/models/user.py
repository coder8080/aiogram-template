from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from sqlalchemy.sql.sqltypes import BigInteger

from src.models.database import Base, sessionmaker


class User(Base):
    __tablename__ = "user_account"

    chat_id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, index=True)
    blockers: Mapped[list["Blocker"]] = relationship(back_populates="user")


class Blocker(Base):
    __tablename__ = "blocker"

    message_id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, index=True)
    user_id: Mapped[User] = mapped_column(ForeignKey("user_account.chat_id"))

async def create_user(chat_id: int) -> None:
    async with sessionmaker() as session:
        async with session.begin():
            user = User(chat_id=chat_id)

            session = sessionmaker()

            await session.begin()
            session.add(user)
            await session.close()

async def get_user(chat_id: int) -> User | None:
    async with sessionmaker() as session:
        async with session.begin():
            query = await session.execute(select(User).where(User.chat_id == chat_id))
            row = query.first()
            if not row:
                return None
            return row[0]
