from algorithm_practice.arrays_algorithms import reverse_list

def test_reverse_list_non_empty():

    list1 = [1]
    list2 = [1,2]
    list3 = [1,2,3]

    assert reverse_list(list1) == list1
    assert reverse_list(list2) == [2,1]
    assert reverse_list(list3) == [3,2,1] 

