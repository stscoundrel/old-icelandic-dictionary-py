from json import load
from typing import Any, Dict


def read_json(path: str) -> Dict[Any, Any] | Any:
    file = open(path)
    raw_data = load(file)
    file.close()

    return raw_data
