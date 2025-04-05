from typing import List

from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.common.db import Base


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(64))

    blockers: Mapped[List["Blocker"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class Blocker(Base):
    __tablename__ = "blocker"

    message_id: Mapped[int] = mapped_column(
        BigInteger(), primary_key=True, index=True
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship(back_populates="blockers")
