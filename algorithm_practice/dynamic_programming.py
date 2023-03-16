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