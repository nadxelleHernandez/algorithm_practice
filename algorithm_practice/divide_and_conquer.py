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
