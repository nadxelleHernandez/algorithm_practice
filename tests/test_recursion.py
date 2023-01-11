from algorithm_practice.recursion import (factorial,reverse,bunny,
               is_nested_parens,search)
import pytest

def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_positive_num():
    assert factorial(5) == 5 * 4 * 3 * 2 * 1


def test_factorial_negative_num():
    with pytest.raises(ValueError):
        factorial(-1)

def test_reverse_word():
    assert reverse("hello") == "olleh"


def test_reverse_single_character():
    assert reverse("a") == "a"


def test_reverse_empty_string():
    assert reverse("") == ""

def test_bunny_zero_bunnies():
    assert bunny(0) == 0


def test_bunny_one_bunny_has_two_ears():
    assert bunny(1) == 2

def test_bunny_four_bunnies():
    assert bunny(4) == 8

def test_bunny_fifty_bunnies_have_100_ears():
    assert bunny(50) == 100

def test_is_nested_parens():
    parens = "((()))"

    assert is_nested_parens(parens)


def test_is_nested_parens_empty_str():
    assert is_nested_parens("")


def test_is_nested_parens_not_matching_length():
    parens = "((())())"

    assert not is_nested_parens(parens)

def test_is_nested_parens_all_one_side():
    parens = "))))"

    assert not is_nested_parens(parens)

def test_search_success_unsorted():
    assert search(["b", "c", "a"], "a")


def test_search_empty_array():
    assert not search([], "a")


def test_search_success_first_item():
    assert search(["a", "b", "c"], "a")


def test_search_not_found():
    assert not search(["a", "b", "c"], "🌈")