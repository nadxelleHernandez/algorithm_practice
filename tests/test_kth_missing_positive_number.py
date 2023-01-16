from algorithm_practice.arrays_algorithms import kth_missing_positive_number

def test_kth_missing_positive_number_valid_inputs():
    # arrange
    arr = [3,4,8]
    k = 7

    # act
    result = kth_missing_positive_number(arr,k)
    
    # assert
    assert result == 10

def test_kth_missing_positive_number_empty_array():
    arr = []
    k = 2

    # act
    result = kth_missing_positive_number(arr,k)
    
    # assert
    assert result == 2

def test_kth_missing_positive_number_finds_num_before_entire_given_list():
    # Arrange
    list = [2,3,4,7,11]
    k = 1

    # Act
    answer = kth_missing_positive_number(list, k)

    # Assert
    assert 1 == answer

def test_kth_missing_number_finds_num_near_end_of_list():
    # Arrange
    list = [2,3,4,7,11]
    k = 5

    # Act
    answer = kth_missing_positive_number(list, k)

    # Assert
    assert 9 == answer

def test_kth_missing_positive_number_finds_num_after_entire_given_list():
    # Arrange
    list = [1,2,3,4]
    k = 2

    # Act
    answer = kth_missing_positive_number(list, k)

    # Assert
    assert 6 == answer

def test_kth_missing_positive_number_2nd_number_before_list_starts():
    # Arrange
    list = [3,4,5,7,11]
    k = 2

    # Act
    answer = kth_missing_positive_number(list, k)

    assert 2 == answer