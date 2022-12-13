from algorithm_practice.arrays_algorithms import send_smallest_to_front

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