from algorithm_practice.string_algorithms import camelcase, marsExploration, reverseWords
import pytest

def test_camelcase_camelcase_string():
    s = "camelCaseString"

    result = camelcase(s)

    assert result == 3

def test_marsExploration_altered_SOS():
    s = "SOSSPSSQSSOR"

    result = marsExploration(s)

    assert result == 3

def test_marsExploration_non_altered_SOS():
    s = "SOSSOSSOSSOS"

    result = marsExploration(s)

    assert result == 0


def test_marsExploration_empty_SOS():
    with pytest.raises(ValueError):
        marsExploration("")

def test_marsExploration_incomplete_SOS():
    with pytest.raises(ValueError):
        marsExploration("SOSSPSSQSSO")

def test_reverse_words():
    s = "the sky is blue"

    r = reverseWords(s)

    assert r == "blue is sky the"

def test_reverse_words_spaces_in_both_ends():
    s = "  hello world  "
    r = reverseWords(s)

    assert r == "world hello"
