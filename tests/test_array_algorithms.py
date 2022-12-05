import pytest

from algorithm_practice.arrays_algorithms import concatenate_lists, send_smallest_to_front, reverse_list, is_palindrome 

def test_concatenate_lists_non_empty_lists():
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    added_list = concatenate_lists(list1,list2)

    assert len(added_list) == 6
    assert added_list == ["a", "b", "c", 1, 2, 3]

def test_concatenate_lists_one_empty_parameter():
    list1 = ["a", "b", "c"]
    list2 = []

    added1 = concatenate_lists(list1,list2)
    added2 = concatenate_lists(list2,list1)
    added3 = concatenate_lists(list1,None)
    added4 = concatenate_lists(None,list1)

    assert added1 == added2 == added3 == added4 == list1

def test_concatenate_lists_num_parameters():
    list1 = [1, 2, 3]

    added1 = concatenate_lists(list1,1)
    added2 = concatenate_lists(2,list1)
    added3 = concatenate_lists(1,2)

    assert added1 == [1, 2, 3, 1]
    assert added2 == [2, 1, 2, 3]
    assert added3 == [1,2]

def test_smallest_to_front_int_array():
    list1 = [3, 4, 2, 9, 1, 8, 7, 6]
    list2 = [3, 4, 2, 9, 1, 8, 1, 7, 6]

    smallest1 = send_smallest_to_front(list1)
    smallest2 = send_smallest_to_front(list2)

    assert smallest1 == [1, 3, 4, 2, 9, 8, 7, 6]
    assert smallest2 == [1, 3, 4, 2, 9, 8, 1, 7, 6]

def test_smallest_to_front_smallest_is_last():
    list1 = [3, 4, 2, 9, 1, 8, 7, 0]

    smallest = send_smallest_to_front(list1)

    assert smallest == [0, 3, 4, 2, 9, 1, 8, 7]

def test_smallest_to_front_smallest_is_first():
    list1 = [-1, 4, 2, 9, 1, 8, 7, 0]

    smallest = send_smallest_to_front(list1)

    assert smallest == list1

def test_smallest_to_front_empty_none_list():

    smallest1 = send_smallest_to_front([])
    smallest2 = send_smallest_to_front(None)

    assert smallest1 == []
    assert smallest2 == None

def test_reverse_list_non_empty():

    list1 = [1]
    list2 = [1,2]
    list3 = [1,2,3]

    assert reverse_list(list1) == list1
    assert reverse_list(list2) == [2,1]
    assert reverse_list(list3) == [3,2,1] 

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



