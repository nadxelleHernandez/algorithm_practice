from algorithm_practice.arrays_algorithms import duplicates_within_k
import pytest

def test_duplicates_within_k_valid_inputs_true_duplicates():
    array = [1, 0, 2, 1, 3, 4]
    k = 5

    result = duplicates_within_k(array,k)

    assert result

def test_duplicates_within_k_valid_inputs_no_duplicates():
    array = [1, 0, 2, 1, 3, 4]
    k = 1

    result = duplicates_within_k(array,k)

    assert not result

def test_duplicates_within_k_returns_true_when_not_first_subarray():
    array = [5,6,2,0,3,0,1]
    k = 2

    result = duplicates_within_k(array,k)

    assert result

def test_duplicates_within_k_returns_false_when_duplicates_out_of_k():
    array = [5,6,2,0,3,1,0]
    k = 2

    result = duplicates_within_k(array,k)

    assert not result


