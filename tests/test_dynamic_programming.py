from algorithm_practice.dynamic_programming import longest_common_subsequence, max_contiguous_sum

def test_lcs_two_str_and_subsequence():
    str1 = "abcde"
    str2 = "ace"

    result = longest_common_subsequence(str1, str2)

    assert result == 3

def test_max_contiguous_sum_valid_array():
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]

    result = max_contiguous_sum(arr)

    assert result == 7

    