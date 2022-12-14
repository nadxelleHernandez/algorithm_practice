from algorithm_practice.arrays_algorithms import rotate_list

def test_rotate_list_non_empty_number_lists():
    arr = [5, 8, 1, 3, 7, 6]
    num = 3  

    result = rotate_list(arr,num)

    assert len(result) == len(arr)
    assert result == [3, 7, 6, 5, 8, 1]

def test_rotate_list_non_empty_lists():
    arr = ["mine","yours","they","them"]
    num = 2  

    result = rotate_list(arr,num)

    assert len(result) == len(arr)
    assert result == ["they","them","mine","yours"]

def test_rotate_list_empty_list():
    arr = []
    num = 2  

    result = rotate_list(arr,num)

    assert len(result) == len(arr)
    assert result == []

def test_rotate_list_non_empty_lists_shift_by_len_multiple():
    arr = [5, 8, 1, 3, 7, 6]
    num1 = 6  
    num2 = 60

    result1 = rotate_list(arr,num1)
    result2 = rotate_list(arr,num2)

    assert result1 == result2
    assert len(result1) == len(arr)
    assert result1 == [5, 8, 1, 3, 7, 6]