def rotate_90(matrix):
    '''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
        Input: matrix = [[1,2,3],
                         [4,5,6],
                         [7,8,9]]
        Output: [[7,4,1],
                 [8,5,2],
                 [9,6,3]]

        Input: matrix = [[5,1,9,11],
                         [2,4,8,10],
                         [13,3,6,7],
                         [15,14,12,16]]
        Output: [[15,13,2,5],
                [14,3,4,1],
                [12,6,8,9],
                [16,7,10,11]]
    '''
    n = len(matrix) #fliping over the horizontal
    for i in range(n//2):
       for j in range(n):
          temp = matrix[i][j]
          matrix[i][j] = matrix[n-1-i][j]
          matrix[n-1-i][j] = temp
           
    
    #flipping by the diagonal the middle
    for i in range(n):
        j = i + 1
        while j < n:
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            j += 1

    return matrix


#   [1,2,3,4]
#   [1,2,3,4]
#   [1,2,3,4]
#   [1,2,3,4]
# ]
# 
# n, n -1, n-1, n - 2, n - 2, n - 3, n - 3, done
#
# [
#   [1,2,3,4,5]
#   [1,2,3,4,5]
#   [1,2,3,4,5]
#   [1,2,3,4,5]
#   [1,2,3,4,5]
# ]
# ]
# # n, n -1, n-1, n - 2, n - 2, n - 3, n - 3, n - 4, n - 4, done
#
# Prints out the array elements in a spiral, starting from (0, 0) and going right
# Example:
# 1 2 3 6 9 8 7 4 5

# if is empty print message
# have indexes for row and other for the column
#start them in zero
def printSpiral(matrix):
    if not matrix:
        return []
    
    x = 0
    y = 0

    x_times_max = len(matrix)
    y_times_max = x_times_max
    d = 1
    
    spiral = []
    while x_times_max > 0 and y_times_max > 0:
        x_count = 0
        y_count = 0
        while y_count < y_times_max:
            spiral.append(matrix[x][y])
            y += d
            y_count += 1
        
        x_times_max -= 1 
        x += d
        y += d*(-1)
        while x_count < x_times_max:
            spiral.append(matrix[x][y])
            x += d
            x_count += 1
        
        y_times_max -=1
        d *= -1
        x += d
        y += d

    return spiral


def reshape_matrix(matrix, r, c):
    '''You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the number of rows and number of columns of the wanted reshaped matrix, respectively.
        The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
        If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
            Example 1:
            Input: 
            nums = 
            [[1,2],
            [3,4]]
            r = 1, c = 4

            Output: 
            [[1,2,3,4]]
        '''

    if not matrix:
        return []

    if r <= 0 or c <=0:
        return matrix

    total_elements = 0
    is_matrix = True
    if type(matrix[0]) is list:
        total_elements = len(matrix) * len(matrix[0])
    else:
        total_elements = len(matrix)
        is_matrix = False

    if r * c != total_elements:
        return matrix

    i = 0
    actual_row = []
    new_matrix = []
    if is_matrix:
        for row in matrix:
            for col in row:
                if i < c:
                    actual_row.append(col)
                    i += 1
                else:
                    new_matrix.append(actual_row)
                    actual_row = list()
                    actual_row.append(col)
                    i = 1
    else:
        for col in matrix:
            if i < c:
                actual_row.append(col)
                i += 1
            else:
                new_matrix.append(actual_row)
                actual_row = list()
                actual_row.append(col)
                i = 1
                
    new_matrix.append(actual_row)
    return new_matrix
