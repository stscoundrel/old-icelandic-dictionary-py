# Old Icelandic Dictionary

Old Icelandic dictionary for Python. From "A Concise Dictionary of Old Icelandic" by Geir Zoëga

The dictionary consists of 29 000+ Old Icelandic words with English translations.

### Install

`pip install old-icelandic-dictionary`

### Usage

The dictionary comes in two variants:
- Default dictionary has html markup `<i>` and `<b>` to match look of the original book.
- No-markup version has the same content without any additional formatting tags.

```python

from old_icelandic_dictionary import get_default, get_no_markup

# Both dictionaries return entries that consist of word definition, and definitions list.
default = get_default()
no_markup = get_no_markup()

# Headwords wont differ between dictionaries.
print(default[14].word)   # afbindi
print(no_markup[14].word) # afbindi

# But definition markup does differ.
print(default[14].definitions[0])   # n. <i>constipation</i>.
print(no_markup[14].definitions[0]) # n. constipation.

```

Individual words are returned in format of:

```python
{
    word: str
    definitions: Tuple[str, ...]
}
```

### About "A Concise Dictionary of Old Icelandic"

"A Concise Dictionary of Old Icelandic" dictionary was published in 1910 by Geir Zoëga, which leads to there being many public domain versions of the book available. Zoëgas attempt was to made easier-to-approach version of the more full Cleasby - Vigfusson dictionary, specifically for beginners and those interested in Old Icelandic prose writing.