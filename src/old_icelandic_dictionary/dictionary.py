import os
from . import reader
from enum import Enum
from typing import NamedTuple, Tuple


class DictionaryPath(str, Enum):
    DEFAULT = os.path.dirname(__file__) + "/resources/default.json"
    NO_MARKUP = os.path.dirname(__file__) + "/resources/no-markup.json"


class DictionaryEntry(NamedTuple):
    word: str
    definitions: Tuple[str, ...]


def get_dictionary(path: str) -> Tuple[DictionaryEntry, ...]:
    raw_data = reader.read_json(path)

    return tuple(
        DictionaryEntry(raw_entry["word"], raw_entry["definitions"])
        for raw_entry in raw_data
    )
