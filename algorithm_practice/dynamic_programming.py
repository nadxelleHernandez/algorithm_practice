def fibonacci(n):
    if n == 0 or n == 1:
        return n

    solutions = [0, 1]
    current = 2

    while current <= n:
        solutions.append(solutions[current - 1] + solutions[current - 2])
        current += 1

    return solutions[n]

def fibonacci_recursive(n, solutions=None):
    '''
    Using dynamic programing
    '''
    if solutions is None:
        solutions = {}

    if n in solutions:
        return solutions[n]

    if n == 0 or n == 1:
        solutions[n] = n
    else:
        solutions[n] = (fibonacci_recursive(n - 1, solutions) +
            fibonacci_recursive(n - 2, solutions))

    return solutions[n] 

def longest_common_subsequence(str1, str2, memo=None):
    '''
    Input: Two strings to compare, memo= dictionary to save preview calculated subsequences
    Output:
    str1= abcde
    str2= ace
    subsequence = ace
    returns 3

    str1= abcde
    str2= aqzcrwe
    subsequence = ace
    returns 3

    str1= abc
    str2= def
    subsequence = ""
    returns 0
    '''
    if not str1 or not str2:
        return 0

    # initialize the memo or lookup the current values
    if memo is None:
        memo = {}
    elif str1 not in memo:
        memo[str1] = {}
    elif str2 in memo[str1]:
        return memo[str1][str2]

    first1 = str1[0]
    rest1 = str1[1:]
    first2 = str2[0]
    rest2 = str2[1:]

    if first1 == first2:
        current_score = 1
    else:
        current_score = 0

    result = max(
        # include the memo in the recursive calls
        current_score + longest_common_subsequence(rest1, rest2, memo),
        longest_common_subsequence(rest1, str2, memo),
        longest_common_subsequence(str1, rest2, memo)
    )

    # store this calculation for later
    memo[str1][str2] = result

    return result

def max_contiguous_sum(arr):
    '''
    INPUT: 1-dimensional array with integers which can be either positive or negative
    OUTPUT: int, which is the maximum contiguous subarray sum

    Example input:
    [-2, -3, 4, -1, -2, 1, 5, -3]

    Example output:
    7 (from index 2-6)
    '''
    if not arr:
        return 0
    
    max_sum = arr[0]
    length = len(arr)

    if length == 1:
        return max_sum

    i = 1
    j = 0
    sum = 0

    while j < length:
        sum += arr[j]
        if max_sum < sum:
            max_sum = sum
        if sum < 0:
            sum = 0
        j+=1

    return max_sum

    # while j < length:
    #     sum += arr[j]
    #     if arr[i] >= max_sum or sum > max_sum:
    #         max_sum = max(arr[i],sum)
            
    #     else:
    #         i += 1
    #         sum = arr[i]
    #         j = i

    #     j += 1
        # sum = arr[i] + arr[j]
        # if arr[i] > max_sum or sum > max_sum: #The sum is increasing
        #     max_sum = max(arr[i],sum)
        #     actual_sum += sum
        # else:
        #     actual_sum = 0
        # i += 1 
        # j += 1

    return max_sum
    