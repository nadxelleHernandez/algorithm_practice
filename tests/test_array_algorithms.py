from algorithm_practice.arrays_algorithms import merge,intersect, intersect_sorted, add_one_int_array

def test_merge():
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]

    merge(nums1,3,nums2,3)

    assert nums1 == [1,2,2,3,5,6]

def test_intersect():
    nums1 = [1,2,2,1]
    nums2 = [2,2]

    result = intersect(nums1,nums2)

    assert result == [2,2]

def test_intersect_sorted():
    nums1 = [1,1,2,2,3,4,5]
    nums2 = [2,2,5,8]

    result = intersect_sorted(nums1,nums2)

    assert result == [2,2,5]

def test_add_one_int_array_no_carry_on():
    digits = [1,2,3]

    result = add_one_int_array(digits)

    assert result == [1,2,4]

def test_add_one_int_array_carry_on():
    digits = [1,9,9]

    result = add_one_int_array(digits)

    assert result == [2,0,0]

def test_add_one_int_array_one_element_carry_on():
    digits = [9]

    result = add_one_int_array(digits)

    assert result == [1,0]