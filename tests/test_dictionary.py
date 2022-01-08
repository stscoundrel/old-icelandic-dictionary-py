from src import old_icelandic_dictionary


def test_default_dictionary_has_correct_length() -> None:
    result = old_icelandic_dictionary.get_default()
    assert len(result) == 29951


def test_default_dictionary_has_expected_content() -> None:
    result = old_icelandic_dictionary.get_default()

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
    result = old_icelandic_dictionary.get_no_markup()
    assert len(result) == 29951


def test_no_markup_dictionary_has_expected_content() -> None:
    result = old_icelandic_dictionary.get_no_markup()

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
    dictionary = old_icelandic_dictionary.get_default()
    no_markup_dictionary = old_icelandic_dictionary.get_no_markup()

    for index, entry in enumerate(dictionary):
        assert entry.word == no_markup_dictionary[index].word
