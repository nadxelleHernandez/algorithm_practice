import pytest
from algorithm_practice.arrays_algorithms import is_palindrome

def test_is_palindrome_valid_input_same_case():
    string1 = "kayak"
    string2 = "kayak noon kayak"

    result1 = is_palindrome(string1)
    result2 = is_palindrome(string2)

    assert result1
    assert result2

def test_is_palindrome_case_insensitive():
    string = "Noon 1 noon"

    result = is_palindrome(string)

    assert result

def test_is_palindrome_non_string_iterable_argument():
    input_val = [1,2,3,2,1]

    result = is_palindrome(input_val)

    assert result

def test_is_palindrome_none_argument_raise_exception():
    with pytest.raises(ValueError):
        is_palindrome(None)

def test_is_palindrome_non_iterable_argument_raise_exception():
    with pytest.raises(ValueError):
        is_palindrome(2)

def test_is_palindrome_no_string():
    result = is_palindrome("")
    assert not result