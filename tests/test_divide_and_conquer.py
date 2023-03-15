from algorithm_practice.divide_and_conquer import smallest_missing_num

def test_smallest_missing_num_valid_array_with_missing_number():
    arr = [0, 1, 2, 6, 9, 11, 15]

    result = smallest_missing_num(arr)

    assert result == 3

def test_smallest_missing_num_valid_array_with_number_zero_missing():
    arr = [ 1, 2, 6, 9, 11, 15]

    result = smallest_missing_num(arr)

    assert result == 0

def test_smallest_missing_num_valid_array_with_none_missing():
    arr = [0, 1, 2, 3, 4, 5, 6]

    result = smallest_missing_num(arr)

    assert result == 7

def test_smallest_missing_num_valid_array_missing_on_left():
    arr = [0, 1, 2, 3, 6, 7]

    result = smallest_missing_num(arr)

    assert result == 4

def test_smallest_missing_num_valid_array_missing_last():
    arr = [0, 1, 2, 3, 4, 5, 7]

    result = smallest_missing_num(arr)

    assert result == 6
