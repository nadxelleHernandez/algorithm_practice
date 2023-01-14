from algorithm_practice.sort_algorithms import sort_by_length, insert_sort, merge_sort

def test_insert_sort():
    lst = [3,0,5,8,9,1]
    result = insert_sort(lst)
    assert result == [0,1,3,5,8,9]

def test_insert_sort_one_swap():
    lst = [2,3,4,5,1]
    result = insert_sort(lst)
    assert result == [1,2,3,4,5]

def test_sort_by_length_with_empty_string():
    assert sort_by_length("") == []


def test_sort_by_length():
    assert sort_by_length("I love great awesome words") == [
        "I", "love", "great", "words", "awesome"]


def test_sort_by_length_checks_smallest_word_last():
    assert sort_by_length("love great awesome words I") == [
        "I", "love", "great", "words", "awesome"]


def test_sort_by_length_equal_length_maintains_order():
    assert sort_by_length("words of equal length") == [
        "of", "words", "equal", "length"]

def test_merge_sort_valid_input():
    array = [3,0,5,8,9,1,5,10,4]
    sorted = merge_sort(array)

    assert sorted == [0,1,3,4,5,5,8,9,10]