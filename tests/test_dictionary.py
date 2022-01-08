from src.old_icelandic_dictionary.dictionary import DictionaryPath, get_dictionary


def test_default_dictionary_has_correct_length() -> None:
    result = get_dictionary(DictionaryPath.DEFAULT)
    assert len(result) == 29951


def test_default_dictionary_has_expected_content() -> None:
    result = get_dictionary(DictionaryPath.DEFAULT)

    assert result[14].word == "afbindi"
    assert result[14].definitions[0] == "n. <i>constipation</i>."

    assert result[1000].word == "andstreymr"
    assert (
        result[1000].definitions[0]
        == "a. <i>strongly adverse</i> (andstreym ørlög); Sighvatr var heldr ~ um eptirmálin, <i>hard to come to terms with</i>."
    )

    assert result[25000].word == "undanhald"
    assert result[25000].definitions[0] == "n. <i>flight</i>."


def test_no_markup_dictionary_has_correct_length() -> None:
    result = get_dictionary(DictionaryPath.NO_MARKUP)
    assert len(result) == 29951


def test_no_markup_dictionary_has_expected_content() -> None:
    result = get_dictionary(DictionaryPath.NO_MARKUP)

    assert result[14].word == "afbindi"
    assert result[14].definitions[0] == "n. constipation."

    assert result[1000].word == "andstreymr"
    assert (
        result[1000].definitions[0]
        == "a. strongly adverse (andstreym ørlög); Sighvatr var heldr ~ um eptirmálin, hard to come to terms with."
    )

    assert result[25000].word == "undanhald"
    assert result[25000].definitions[0] == "n. flight."


def test_dictionary_headwords_match() -> None:
    dictionary = get_dictionary(DictionaryPath.DEFAULT)
    no_markup_dictionary = get_dictionary(DictionaryPath.NO_MARKUP)

    for index, entry in enumerate(dictionary):
        assert entry.word == no_markup_dictionary[index].word
