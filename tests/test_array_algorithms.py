from algorithm_practice.arrays_algorithms import merge,intersect, intersect_sorted, add_one_int_array, moveZeroes, two_sum, isValidSudoku, has_word

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

def test_moveZeroes_non_empty_array_with_zeroes():
    nums = [0,1,0,3,12]

    moveZeroes(nums)

    assert nums == [1,3,12,0,0]

def test_two_sum_non_empty_positive_pair_exists():
    nums = [2,7,11,15]
    target = 9

    result = two_sum(nums,target)

    assert len(result) == 2
    assert 0 in result
    assert 1 in result

def test_two_sum_non_empty_negatives_pair_exists():
    nums = [-2,21,5,-11,8]
    target = -13

    result = two_sum(nums,target)

    assert len(result) == 2
    assert 0 in result
    assert 3 in result

def test_two_sum_same_pair_sum_exists():
    nums = [3,3,-1]
    target = 6

    result = two_sum(nums,target)

    assert len(result) == 2
    assert 0 in result
    assert 1 in result

def test_two_sum_same_number_other_pair_exists():
    nums = [3,2,4]
    target = 6

    result = two_sum(nums,target)

    assert len(result) == 2
    assert 1 in result
    assert 2 in result


def test_isValidSudoku_Valid_board():
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    assert isValidSudoku(board)

def test_isValidSudoku_invalid_Board():
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    assert isValidSudoku(board) == False

def test_isValidSudoku_extrem_board():
    board = [[".",".",".",".",".",".","5",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,["9","3",".",".","2",".","4",".","."]
            ,[".",".","7",".",".",".","3",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".","3","4",".",".",".","."]
            ,[".",".",".",".",".","3",".",".","."]
            ,[".",".",".",".",".","5","2",".","."]]
    
    assert isValidSudoku(board) == False

def test_has_word_hackerrank_true_many_repetitions():
    word = "hackerrankk"
    s = "hereIamathackernomorerrankkk"

    assert has_word(s,word)

def test_has_word_mucho_false():
    word = "mucho"
    s = "noestamuybieno"

    assert not has_word(s,word)