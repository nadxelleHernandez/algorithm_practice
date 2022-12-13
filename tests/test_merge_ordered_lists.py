from algorithm_practice.arrays_algorithms import merge_ordered_lists

def test_merge_ordered_lists_same_len_non_empty():
    list1 = [-30, -10, 0, 15, 16]
    list2 = [-20, -5, 5, 6, 10]

    result = merge_ordered_lists(list1, list2)

    assert len(result) == 10
    assert result == [-30,-20,-10,-5,0,5,6,10,15,16]

def test_merge_ordered_lists_list1_shorter_non_empty():
    list1 = [-20, -5, 5]
    list2 = [-30, -10, 0, 15, 16]

    result = merge_ordered_lists(list1, list2)

    assert len(result) == 8
    assert result == [-30, -20, -10, -5, 0, 5, 15, 16]

def test_merge_ordered_lists_list2_shorter_non_empty():
    list1 = [-30, -10, 0, 15, 16]
    list2 = [-20, -5, 5]

    result = merge_ordered_lists(list1, list2)

    assert len(result) == 8
    assert result == [-30, -20, -10, -5, 0, 5, 15, 16]

def test_merge_ordered_lists_first_list_goes_all_first():
    list1 = [-1,0,1,2]
    list2 = [3,9,10]

    result = merge_ordered_lists(list1, list2)

    assert len(result) == 7
    assert result == [-1,0,1,2,3,9,10]

def test_merge_ordered_lists_second_list_goes_all_first():
    list2 = [-1,0,1,2]
    list1 = [3,9,10]

    result = merge_ordered_lists(list1, list2)

    assert len(result) == 7
    assert result == [-1,0,1,2,3,9,10]

def test_merge_ordered_lists_first_list_empty():
    list1 = []
    list2 = [3,9,10]

    result = merge_ordered_lists(list1, list2)

    assert len(result) == 3
    assert result == [3,9,10]

def test_merge_ordered_lists_second_list_empty():
    list1 = [-1,0,1,2]
    list2 = []

    result = merge_ordered_lists(list1, list2)

    assert len(result) == 4
    assert result == [-1,0,1,2]

def test_merge_ordered_lists_both_empty():
    list1 = []
    list2 = []

    result = merge_ordered_lists(list1, list2)

    assert len(result) == 0
    assert result == []

def test_merge_ordered_lists_with_same_number_both_lists():
    lst1 = [1,3,4,5]
    lst2 = [-1,0,1,2]

    # act
    result = merge_ordered_lists(lst1,lst2)

    # assert
    assert len(result) == 8
    assert result == [-1,0,1,1,2,3,4,5]

def test_merge_ordered_lists_with_duplicates_in_any_list():
    lst1 = [1,3,4,5,5]
    lst2 = [-1,0,1,2]

    # act
    result = merge_ordered_lists(lst1,lst2)

    # assert
    assert len(result) == 9
    assert result == [-1,0,1,1,2,3,4,5,5]

def test_merge_ordered_lists_with_sorted_non_numbers_elements():
    list1 = ['a','c','e']
    list2 = ['b','f','g','h','j','k']

    result = merge_ordered_lists(list1, list2)

    assert len(result) == 9
    assert result == ['a', 'b','c', 'e','f','g','h','j','k']





