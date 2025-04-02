from os import getenv
from typing import cast

TOKEN = cast(str, getenv("TOKEN"))
LOCAL = bool(getenv("LOCAL"))
POSTGRES_USER = cast(str, getenv("POSTGRES_USER"))
POSTGRES_PASSWORD = cast(str, getenv("POSTGRES_PASSWORD"))

assert TOKEN
assert POSTGRES_USER
assert POSTGRES_PASSWORD


TEXT = {"start": "Hello world"}
