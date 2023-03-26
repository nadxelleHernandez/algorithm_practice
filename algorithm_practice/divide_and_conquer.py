def smallest_missing_num(nums):
    '''
    INPUT: 1-dimensional array with integers 
    OUTPUT: The integer which represents the smallest missing non-negative element inside of the array. 
    If the array contains all of the elements, return the smallest number following the length of the array.

    Example input:
    [0, 1, 2, 6, 9, 11, 15]

    Example output:
    3
    '''
    if not nums:
        return None
    
    nums_len = len(nums)
    if nums[0] != 0:
        return 0
    
    ini = 0
    end = nums_len - 1
    mid = nums_len // 2

    while ini != end - 1:
        if nums[mid] > mid:
            end = mid
        elif nums[mid] == mid: #The array is complete on he left, need to search on the right
            ini = mid
        mid = (ini + end) // 2
        
    if nums[nums_len - 1]!= nums_len - 1:
        return ini + 1
    else:
        return nums_len     
    
def pascal_triangle(n):
    '''
    Input: num_rows = 3
    Output: [[1], [1, 1], [1, 2, 1]]
    Explanation: The 0th index (first row) in the outer list contains one number: [1]. 
    The 1st index (second row) contains two numbers: [1, 1]. 
    The 2nd index (third row) can be calculated by setting the first and last indexes to 1 
    and calculating the middle index using the two elements above it (1 + 1) 
    so the third row is [1, 2, 1].

    Input: num_rows = 3
    Output: [[1], [1, 1], [1, 2, 1]]
    Explanation: The 0th index (first row) in the outer list contains one number: [1]. 
    The 1st index (second row) contains two numbers: [1, 1]. 
    The 2nd index (third row) can be calculated by setting the first and last indexes to 1 
    and calculating the middle index using the two elements above it (1 + 1) 
    so the third row is [1, 2, 1].
    '''

    if n < 0:
        return None
    
    if n == 0:
        return []
    
    triangle = [[1]]
    if n == 1:
        return triangle
    
    triangle.append([1,1])
    if triangle == 2:
        return triangle
    
    for i in range(2,n):
        triangle.append([1])
        prev_row = triangle[i-1]
        prev_row_len = len(prev_row) - 1 #could be reduced to half
        for j in range(prev_row_len):
            triangle[i].append(prev_row[j]+prev_row[j+1])

        triangle[i].append(1)

    return triangle

