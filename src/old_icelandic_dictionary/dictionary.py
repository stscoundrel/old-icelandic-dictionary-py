import os
from typing import NamedTuple, Tuple
from json import load
from strenum import StrEnum

class DictionaryPath(StrEnum):
    DEFAULT = os.path.dirname(__file__)+'/resources/dictionary.json'


class DictionaryEntry(NamedTuple):
    word: str
    definitions: Tuple[str, ...]


def get_dictionary(path: str) -> Tuple[DictionaryEntry, ...]:
    file = open(path) 
    raw_data = load(file)
    file.close()

    return tuple( DictionaryEntry(raw_entry['word'], raw_entry['definitions']) for raw_entry in raw_data)



