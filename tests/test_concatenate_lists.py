import pytest

from algorithm_practice.arrays_algorithms import concatenate_lists

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