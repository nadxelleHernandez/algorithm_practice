from algorithm_practice.dynamic_programming import longest_common_subsequence, newman_conway, minimum_sub_list_length
from algorithm_practice.arrays_algorithms import max_contiguous_sum

def test_minimum_sub_list_length():
    arr = [3, 2, 5, 8, 12, 1]
    k = 5

    result = minimum_sub_list_length(arr,k)

    assert result == 1

def test_minimum_sub_list_length_1234_target_10():
    arr = [1,2,3,4]
    k = 10

    result = minimum_sub_list_length(arr,k)

    assert result == 4

def test_newman_conway_n_2():
    newman = newman_conway(2)

    assert newman == 1

def test_newman_conway_n_5():
    newman = newman_conway(5)

    assert newman == 3

def test_newman_conway_n_8():
    newman = newman_conway(8)

    assert newman == 4

def test_newman_conway_n_20():
    newman = newman_conway(20)

    assert newman == 12

def test_lcs_two_str_and_subsequence():
    str1 = "abcde"
    str2 = "ace"

    result = longest_common_subsequence(str1, str2)

    assert result == 3

def test_lcs_two_str_and_no_subsequence():
    str1 = "abcde"
    str2 = "fgh"

    result = longest_common_subsequence(str1, str2)

    assert result == 0

def test_lcs_one_str_one_empty_str_returns_no():
    str1 = "abcde"
    str2 = ""

    result = longest_common_subsequence(str1, str2)

    assert result == 0

def test_lcs_one_str_two_empty_str_returns_no():
    str2 = "abcde"
    str1 = ""

    result = longest_common_subsequence(str1, str2)

    assert result == 0

def test_max_contiguous_sum_valid_array():
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]

    result = max_contiguous_sum(arr)

    assert result == 7

def test_max_contiguous_sum_valid_array_smallest():
    arr = [2,-8,3,2,-5,4,-10]

    result = max_contiguous_sum(arr)

    assert result == 5

