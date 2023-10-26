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
  row =0  
  column = 0
  
  matrix_length = len(matrix[0])
  
  
  
  #In first row, go through each column to the end
  #change row until the end of rows n-1 times
  #change column until the begining n-1 times
  #change rows until last row n-1 times
  #change column until n-1