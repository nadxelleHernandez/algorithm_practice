from algorithm_practice.matrix_algorithms import rotate_90, printSpiral,exist_word

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

def test_word_in_board_exist_valid_word_dublicate_continuous_characters():
    board = [["A","B","C","E"], ["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"

    assert exist_word(board,word)

def test_word_in_board_exist_valid_word_at_the_edge():
    board = [["A","B","C","E"], ["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"

    assert exist_word(board,word)

def test_word_in_board_exist_not_there():
    board = [["A","B","C","E"], ["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"

    assert not exist_word(board,word)

def test_word_in_board_exist_2x2_board():
    board = [["a","b"],
             ["c","d"]]
    word = "acdb"

    assert exist_word(board,word)