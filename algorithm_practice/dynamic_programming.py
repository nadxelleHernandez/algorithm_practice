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

def get_max_sum_subarray_k(arr, k):
    '''
    Given an array of integers and a number k, find the maximum sum of a subarray of size k. 
        Input  : arr[] = {100, 200, 300, 400},  k = 2
        Output : 700

        Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4 
        Output : 39
    '''
    pass

def get_ugly_number(n):
    '''
    Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. 
    By convention, 1 is included. 
    Given a number n, the task is to find n’th Ugly number.

    Input  : n = 7
    Output : 8

    Input  : n = 10
    Output : 12

    Input  : n = 15
    Output : 24

    Input  : n = 150
    Output : 5832
    '''
    pass

def flip_m_zeros_to_max_ones(arr,m):
    '''
    Given a binary array and an integer m, find the position of zeroes flipping 
    which creates maximum number of consecutive 1’s in array.
        Input:   arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
            m = 2
        Output:  5 7
        We are allowed to flip maximum 2 zeroes. If we flip
        arr[5] and arr[7], we get 8 consecutive 1's which is
        maximum possible under given constraints 

        Input:   arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
                m = 1
        Output:  7
        We are allowed to flip maximum 1 zero. If we flip 
        arr[7], we get 5 consecutive 1's which is maximum 
        possible under given constraints.

        Input:   arr[] = {0, 0, 0, 1}
                m = 4
        Output:  0 1 2
        Since m is more than number of zeroes, we can flip
        all zeroes.
    '''
    pass

def min_window_substring(s, t):
    '''
    Given two strings s and t of lengths m and n respectively, return the minimum window
    substring of s such that every character in t (including duplicates) is included in the window. 
    If there is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

        Input: s = "a", t = "a"
        Output: "a"
        Explanation: The entire string s is the minimum window.  

        Input: s = "a", t = "aa"
        Output: ""
        Explanation: Both 'a's from t must be included in the window.
        Since the largest window of s only has one 'a', return empty string.      
    '''
    pass

def  newman_conway_helper(n, memo):
    if n==1 or n==2:
        return 1
    
    if len(memo) > n: #We already calculated it
        return memo[n]
    
    #P(n) = P(P(n - 1) + P(n - P(n - 1)))
    p_of_n_minus_one = memo[n-1] #We for sure have calculated the n-1 one because we go from 3 to n
    return newman_conway_helper(p_of_n_minus_one, memo) + newman_conway_helper(n-p_of_n_minus_one)

def newman_conway_rec(n):
    if n<=0:
        raise 
    memo = [None,1,1]
    if n<= 2:
        return memo[n]
    for i in range(3,n+1):
        next_newman = newman_conway_helper(i,memo)
        memo.append(next_newman)

    return memo[n]

def newman_conway(n):
    if n <= 0:
        return None

    if n <= 2:
        return 1

    memo = [None,1,1]

    #P(n) = P(P(n - 1)) + P(n - P(n - 1))
    for i in range(3,n+1):
        newman_for_i = memo[memo[i-1]] + memo[i-memo[i-1]]
        memo.append(newman_for_i)

    return memo[n]

