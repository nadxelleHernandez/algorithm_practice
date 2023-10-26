from algorithm_practice.matrix_algorithms import rotate_90

def test_rotate_90_4x4_matrix():
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    
    result = rotate_90(matrix)
    print(result)

    assert result == [[7,4,1],
                      [8,5,2],
                      [9,6,3]]