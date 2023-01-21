from algorithm_practice.arrays_algorithms import max_profit

def test_profit_7_1_5_3_6_4():
    # Arrange
    arr = [7, 1, 5, 3, 6, 4]

      # Act
    answer = max_profit(arr)

      # Assert
    assert answer == 7

def test_profit_3_8_2_5_10():
    # Arrange
    arr = [3,8,2,5,10]

      # Act
    answer = max_profit(arr)

      # Assert
    assert answer == 13

def test_profit_1_2_3_4_5():
    # Arrange
    arr = [1, 2, 3, 4, 5]

      # Act
    answer = max_profit(arr)

      # Assert
    assert answer == 4

def test_profit_7_6_4_3_1():
      # Arrange
    arr = [7, 6, 4, 3, 1]

      # Act
    answer = max_profit(arr)

      # Assert
    assert answer == 0