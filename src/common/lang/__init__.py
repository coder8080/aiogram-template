from aiogram.types import User as TgUser


class Lang:
    keys: dict[str, str]

    def __init__(self, keys: dict[str, str]):
        self.keys = keys

    def __call__(self, key: str, actor: TgUser):
        if key not in self.keys:
            raise Exception(f"Language key not found: {key}")

        result = self.keys[key]
        result = result.replace("{%name%}", actor.first_name)
        result = result.replace("{%username%}", actor.username or "unknown")
        result = result.replace("{%id%}", str(actor.id))

        return result
