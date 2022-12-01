import pytest

from algorithm_practice.my_algorithms import concatenate_lists, send_smallest_to_front 

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