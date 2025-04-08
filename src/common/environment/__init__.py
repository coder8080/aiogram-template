from os import getenv


def get_int_env(key: str) -> int:
    str_val = getenv(key)
    assert str_val, f"Can't get required environment variable: {key}"
    assert str_val.isdigit(), f"{key} environment variable is not numeric"
    int_val = int(str_val)
    return int_val


def get_str_env(key: str) -> str:
    val = getenv(key)
    assert val, f"Can't get required enironment variable: {key}"
    return val


def get_bool_env(key: str) -> bool:
    val = getenv(key)
    return val is not None


__all__ = ["get_int_env", "get_str_env", "get_bool_env"]
