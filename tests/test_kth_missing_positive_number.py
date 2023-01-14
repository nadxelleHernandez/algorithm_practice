from algorithm_practice.arrays_algorithms import kth_missing_positive_number

def test_kth_missing_positive_number_valid_inputs():
    # arrange
    arr = [2,3,4,7,11]
    k = 5

    # act
    result = kth_missing_positive_number(arr,5)
    
    # assert
    assert result == 9

def test_kth_missing_positive_number_empty_array():
    arr = []
    k = 2

    # act
    result = kth_missing_positive_number(arr,k)
    
    # assert
    assert result == 2