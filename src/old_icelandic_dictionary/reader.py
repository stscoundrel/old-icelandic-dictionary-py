from json import load
from typing import Any


def read_json(path: str) -> Any:
    file = open(path)
    raw_data = load(file)
    file.close()

    return raw_data
