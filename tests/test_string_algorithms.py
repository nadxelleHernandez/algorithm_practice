from algorithm_practice.string_algorithms import camelcase, marsExploration
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
