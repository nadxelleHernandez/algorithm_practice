from algorithm_practice.arrays_algorithms import merge

def test_merge():
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]

    merge(nums1,3,nums2,3)

    assert nums1 == [1,2,2,3,5,6]