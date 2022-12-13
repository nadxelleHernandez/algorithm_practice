
from algorithm_practice.arrays_algorithms import pairs_with_given_sum

def test_pairs_with_given_sum_all_numerical_input_no_duplicates():
    array1 = [3,2,8,-1,6]
    array2 = [97, 51, 49, 35, 3, 65]
    sum1 = 5
    sum2 = 100

    result1 = pairs_with_given_sum(array1,sum1)
    result2 = pairs_with_given_sum(array2,sum2)

    assert result1 == 2
    assert result2 == 3

def test_pairs_with_given_sum_all_numerical_no_duplicates_sum_is_2x_item():
    list = [3,2,8,-1]
    sum1 = 6

    result = pairs_with_given_sum(list, sum1)

    assert result == 0


def test_pairs_with_given_sum_all_numerical_input_with_duplicates_one_pair():
    arr = [5, 8, 1, 3, 7, 5, 6, 5]
    sum1 = 10

    result = pairs_with_given_sum(arr,sum1)

    assert result == 2

def test_pairs_with_given_sum_all_numerical_input_with_duplicates_many_pairs():
    arr = [5, 8, 1, 3, 7, 5, 6, 5, 5, 5]
    sum1 = 10

    result = pairs_with_given_sum(arr,sum1)

    assert result == 2

def test_pairs_with_given_sum_empty_list():
    arr = []
    sum1 = 10

    result = pairs_with_given_sum(arr,sum1)

    assert result == 0



