from algorithm_practice.matrix_algorithms import rotate_90, printSpiral

def test_rotate_90_4x4_matrix():
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    
    result = rotate_90(matrix)
    print(result)

    assert result == [[7,4,1],
                      [8,5,2],
                      [9,6,3]]
    
def test_spiral_matrix_4X4():
    matrix = [[5,1,8,11],
              [2,4,8,10],
              [13,3,6,7],
              [15,14,12,16]]
    
    result = printSpiral(matrix)

    assert result == [5,1,8,11,10,7,16,12,14,15,13,2,4,8,6,3]

def test_spiral_matrix_3x3():
    matrix = [[5,1,8],
              [2,4,8],
              [13,3,10]]
    
    result = printSpiral(matrix)

    assert result == [5,1,8,8,10,3,13,2,4]

def test_spiral_matrix_2x2():
    matrix = [[1,2],[3,4]]

    result = printSpiral(matrix)

    assert result == [1,2,4,3]

def test_spiral_matrix_1x1():
    matrix = [[1]]

    result = printSpiral(matrix)

    assert result == [1]
