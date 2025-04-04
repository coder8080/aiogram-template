from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
)
from sqlalchemy.orm.decl_api import DeclarativeBase


class Base(DeclarativeBase, AsyncAttrs):
    pass
