from collections.abc import Iterable 
from collections import Counter 

'''
Given two arrays, create your own concatenation function. 
Return a new array containing the first array's values, then the second array's values.
Try not to use built-in methods.  Don't forget edge cases!

Example Input: ["a", "b", "c"], [1, 2, 3]
Example Output: ["a", "b", "c", 1, 2, 3]
'''
def concatenate_array(arr1, arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1

    if not iterable(arr1) or not iterable(arr2):
        return [arr1,arr2]

    concatenated = [i for i in arr1]
    concatenated += arr2

    return concatenated


def iterable(obj):
    return isinstance(obj,Iterable)

def number(obj):
    return type(obj) is int or type(obj) is float
    

def concatenate_lists(lst1, lst2):
    if not lst1 and not lst2:
        return []
    
    if not lst1:
        return list(lst2)

    if not lst2:
        return list(lst1)
    
    iterable1 = lst1
    iterable2 = lst2
    if not iterable(iterable1):
        iterable1 = [iterable1]

    if not iterable(iterable2):
        iterable2 = [iterable2]

    len1 = len(iterable1)
    len2 = len(iterable2)
    added_lists = [None] * (len1+len2)
    index=0
    for elem in iterable1:
        added_lists[index] = elem
        index += 1

    for elem in iterable2:
        added_lists[index] = elem
        index += 1

    return added_lists


def send_smallest_to_front(lst):
    """
    Given an array, find the smallest value and move it to the front of the array. Return the same array. 
    Try not to use built-in methods. Don't forget edge cases!

    Example Input: [3, 4, 2, 9, 1, 8, 7, 6]
    Example Output: [1, 3, 4, 2, 9, 8, 7, 6]

    Example Input: [3, 4, 2, 9, 1, 8, 1, 7, 6]
    Example Output: [1, 3, 4, 2, 9, 8, 1, 7, 6]

    """
    if not lst:
        return lst

    smallest = lst[0]
    smallest_index = 0
    for index in range(len(lst)):
        if lst[index] < smallest:
            smallest = lst[index]
            smallest_index = index

    for i in range(smallest_index-1,-1,-1):
        lst[i+1] = lst[i]
    
    lst[0] = smallest
    return lst
    

def reverse_list(lst):
    """
    Given an array, reverse the order of values without using the built-in method reverse or slice, 
    ie. [: :-1]. Return the same array. Don't forget edge cases!

    Example Input: [1, 2, 3, 4, 5, 6]
    Example Output: [6, 5, 4, 3, 2, 1]
    """
    if not lst:
        return lst

    list_len = len(lst)
    for i in range(list_len//2):
        first = lst[i]
        lst[i] = lst[list_len-i-1]
        lst[list_len-i-1] = first

    return lst

'''
Given an array and number, rotate the values of the array to the right by that number. 
Don't use slice. Return the same array. Don't forget edge cases!

Example Input: [1, 2, 3, 4, 5], 2
Example Output: [4, 5, 1, 2, 3]

Example Input: [1, 2, 3, 4, 5], 5
Example Output: [1, 2, 3, 4, 5]

EXTRA CHALLENGE
Try shifting to the left instead
def rotate_list(list, shift_by):
'''
def rotate_list_n2(lst, shift_by):
    lst_len = len(lst)
    if shift_by >= lst_len and shift_by%lst_len == 0:
        return lst

    for i in range(shift_by):
        lst.insert(0,lst.pop(-1))

    return lst

def rotate_list(lst, shift_by: int):
    if not lst or not shift_by:
        return lst

    lst_len = len(lst)
    shift = shift_by
    if shift >= lst_len:
        if shift%lst_len == 0:
            return lst
        else:
            shift = shift_by%lst_len

    new_list = [0 for x in range(lst_len)]

    j = 0
    for i in range(shift,lst_len):
        new_list[i] = lst[j]
        j += 1

    for i in range(j):
        new_list[i] = lst[j]
        j += 1

    return new_list

def convert_list_to_string(list):
    converted = ""
    for elem in list:
        converted += str(elem)

    return converted

def remove_given_chars(string, removables):
    str_list = list(string)
    for char in string:
        if char in removables:
            str_list.remove(char)

    return convert_list_to_string(str_list)

def is_palindrome(string):
    """
    Write a function that determine if a string is a palindrome

    Don't accept numbers type (raise exception)
    Accept iterables
    trim spaces at the ends
    Accepts special characters (in case we have a frase)

    """
    if string is None or not iterable(string):
        raise ValueError("is_palindrome received an empty or non iterable argument")

    if not string: 
        return False

    if type(string) is not str:
        work_str = convert_list_to_string(string)
    else:
        work_str = string

    str_len = len(work_str)
    for i in range(str_len//2):
        if work_str[i].upper() != work_str[str_len-i-1].upper():
            return False

    return True

def get_n_largest_link(lst,n):
    n_largest = None
    #explore the list creating a linked list size n with the largest
    #insert them ordering them without duplicating
    #start a largest var with the first element of the list
    #insert it to the linked list
    #start a for cicle through the list
    #if the len of list is less than n 
    # insert i[i] it in the right place of the list to keep it ordered

    #finally return the n_largest from the list

    return n_largest

def get_n_largest(array, n):
    """First solution, O(N Log N) time O(n) space"""
    if not array or n > len(array):
        return None

    lst = sorted(array)
    new_list = list()
    
    list_len = len (lst)
    for i in range(list_len-1):
        curr = lst[i]
        next = lst[i+1]
        if curr != next:
            new_list.append(curr)

    if lst[-1] != lst[-2]:
        new_list.append(lst[-1]) 

    if len(new_list) < n:
        return None
    return new_list[-n]

def in_place_remove(lst, start, end):
    """
    Given an array, a start position, and an end position, remove the values within that start-end range "in-place," 
    then return the original array. Don't use slice. Don't forget edge cases!

    Example Input: [5, 8, 1, 3, 7, 5, 6,10], 3, 6
    Example Output: [5, 8, 1, 10]

    Example Input: [4, 5, 6, 7, 10, 11, 12, 13], 5,7
    Example Output: [4, 5, 6, 7, 10]

    Example Input: [4, 5, 6, 7, 10, 11, 12, 13], 7,11
    Example Output: [4, 5, 6, 7, 10, 11, 12]

    """
    if not lst:
        return []

    lst_len = len(lst)
    # handle negative start ends, calculate from there where to start
    if start < 0:
        start = lst_len + start

    if end < 0:
        end =  lst_len + end

    if start > lst_len:
        return lst

    if end >= lst_len:
        end = lst_len-1

    for i in range(end,start-1,-1):
        lst.pop(i)

    return lst

'''Other way to resolve get the n largest'''
def check_num(arr):
    check_list = []
    init = arr[0]
    for i in arr:
        if i > init:
            check_list.append(i)
    return check_list

def find_nth_element(arr, num):
    check_list = []
    init = arr[0]
    if num > len(arr):
        return None 
    if num is None:
        return None 

    if len(check_num(arr)) == num - 1:
        return init
    elif len(check_num(arr)) == num:
        return min(check_num(arr))
    else:
        return check_num(check_list)


def pairs_with_given_sum(lst, target_sum):
    """
    It finds the number of pairs of numbers in a list which add up to a given target. 

    This function should take in a list of whole numbers and a target as parameters. 
    This function should have a return value of the integer of number of pairs.
    numbers:	[1, 2, 4, 5]  
    target: 6	
    Number of pairs (return value) : 2

    """
    if not lst:
        return 0

    helper = dict()
    for num in lst:
        if helper.get(num) is None: #save the duplicates
            helper[num] = 1    
        else:
            helper[num] += 1

    pairs = 0
    for key in helper.keys():
        other_pair_key = target_sum - key
        if other_pair_key == key: 
            if helper[key] >= 2: #we can have a pair of duplicates
                pairs+= 1
                helper[key] = 0
            else:
                continue #the same number can't be used twice
        
        other_pair_val = helper.get(other_pair_key)
        if other_pair_val is not None and other_pair_val > 0: #you can still use it
            pairs += 1
            helper[key] = 0
            helper[other_pair_key] = 0

    return pairs

def merge_ordered_lists(list1, list2):
    if not list1:
        return list2

    if not list2:
        return list1

    merged = list()
    i = 0
    j = 0
    list1_len = len(list1)
    list2_len = len(list2)
    while(True):
        if i == list1_len:  #we finished looping through the first list
            for index in range(j,list2_len):
                merged.append(list2[index]) #we append the rest of the second list
            break
        if j == list2_len: #we finished looping through the second list
            for index in range(i,list1_len):
                merged.append(list1[index])
            break
        if list1[i] <= list2[j]:
            merged.append(list1[i]) #Each number will be added no matter if they are duplicates
            i += 1
        else: # the value on the second list is smaller
            merged.append(list2[j])
            j += 1

    return merged

def merge(nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        totalLen = n+m
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        if n == 0:
            return
        
        res_index = totalLen - 1

        i = m - 1
        j = n - 1

        while i >= 0:
            if j < 0:
                break
            if nums1[i] < nums2[j]:
                nums1[res_index] = nums2[j]
                j = j - 1
                res_index = res_index - 1
            else:
                nums1[res_index] = nums1[i]
                i = i - 1
                res_index = res_index - 1

        while j >= 0:
            nums1[res_index] = nums2[j]
            j = j - 1
            res_index = res_index - 1

def reshape_matrix(matrix, r, c):
    """You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the number of rows and number of columns of the wanted reshaped matrix, respectively.
        The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
        If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
            Example 1:
            Input: 
            nums = 
            [[1,2],
            [3,4]]
            r = 1, c = 4

            Output: 
            [[1,2,3,4]]"""

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

def kth_missing_positive_number(array, k):
    """Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
    Find the kth positive integer that is missing from this array. 
        Input: arr = [2,3,4,7,11], k = 5
        Output: 9
        Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. 
            The 5th missing positive integer is 9.

        Input: arr = [1,2,3,4], k = 2
        Output: 6
        Explanation: The missing positive integers 
            are [5,6,7,...]. The 2nd missing
            positive integer is 6.
    """
        
    if k < 1:
        return None

    if not array:
        return k

    if array[0] < 1:
        return None

    length = len(array)

    if array[0] > k:
        return k

    if array[-1] == length:
        return length + k

    missing_count = array[0]-1
    
    j = 0
    i = array[0]
    missing = 0
    while missing_count != k:
        if j < length and array[j] == i:
            j += 1
        else:
            missing_count += 1
            missing = i
            if j == length: #I'm at the last elemnet of the list. Can calculate the Kth element
                missing = i + k - missing_count
                break
        i += 1   

    return missing

def max_profit(stocks):
    if not stocks:
        return 0

    total_profit = 0
    i = 1
    length = len(stocks)
    while i < length:
        if stocks[i-1] < stocks[i]:
            profit = stocks[i] - stocks[i-1]
            total_profit += profit
        i += 1

    return total_profit

#O(n)2
def has_balanced_sum(array):
    if not array:
        return False

    array_len = len(array)

    if array_len==1:
        return True

    right_sum = 0
    left_sum = 0
    for i in range(1,array_len):
        for j in range(i):
            right_sum+=array[j]
        for j in range(i,array_len):
            left_sum+=array[j]
        if right_sum==left_sum:
            return True
        right_sum = 0
        left_sum = 0
    return False

def get_balanced_sum_index(array):
    if not array:
        return None

    array_len = len(array)

    if array_len==1:
        return 0

    right_sum = 0
    left_sum = 0
    for i in range(1,array_len-1):
        for j in range(i):
            right_sum+=array[j]
        for j in range(i+1,array_len):
            left_sum+=array[j]
        if right_sum==left_sum:
            return i
        right_sum = 0
        left_sum = 0
    return None

def intersect(nums1: [int], nums2: [int]) -> [int]:
    if not nums1:
        return nums2
            
    if not nums2:
        return nums1
        
    rep1 = {}
        
    for num in nums1:
        rep1[num] = rep1.get(num,0) + 1
            
    rep2 = {}
    for num in nums2:
        rep2[num] = rep2.get(num,0) + 1
            
    result = []
    for num in rep1.keys():
        if num in rep2:
            i = 0
            while i < min(rep1[num], rep2[num]):
                result.append(num)
                i += 1
                    
    return result

def intersect_sorted(nums1: [int], nums2: [int]) ->[int]:
    if not nums1:
        return nums2
        
    if not nums2:
        return nums1
        
    len1 = len(nums1)
    len2 = len(nums2)
    i = 0
    j = 0
    result = []
    while i < len1 and j < len2:
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
                j += 1
        else:
            result.append(nums1[i])
            i += 1
            j += 1
                
    return result

def add_one_int_array(number: [int]) -> [int]:
    if not number:
        return [1]
    
    carry_on = 0
    init = len(number)-1
    sum = 0
    for i in range (init,-1,-1):
        if i == init:
            sum = number[i] + 1
        else:
            sum = number[i] + carry_on
        if sum >= 10:
            carry_on = 1
            number[i] = 0
        else:
            number[i] = sum
            carry_on = 0

    if carry_on == 1: 
        number.insert(0,1)

    return number

def moveZeroes(nums: [int]):
    """
        Do not return anything, modify nums in-place instead.
    """
    if not nums: 
        return
        
    non_zero_i = 0
    num_zeros = 0
    nums_len = len(nums)
        
    for i in range(nums_len):
        if nums[i] != 0:
            nums[non_zero_i] = nums[i]
            non_zero_i += 1
    
    for i in range(non_zero_i,nums_len):
        nums[i] = 0


def singleNumber(nums: [int]) -> int:
        '''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
           You must implement a solution with a linear runtime complexity and use only constant extra space.
           
           Input: nums = [2,2,1]
           Output: 1
        '''
        nums.sort()
        
        count = 1 
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count += 1
            else:
                if count == 1:
                    return nums[i]
                count = 1
                
        return nums[-1]

def check_substring(string: str, init: int) -> int:
    used_chars = set()
    current_len = 0
    longest = 0
    slen = len(string)
    for i in range(init,slen):
        if string[i] in used_chars:
            current_len = 1
        else:
            used_chars.add(string[i])
            current_len += 1
        if current_len > longest:
            longest = current_len
    
    return longest
        

def lenght_of_longest_substring(string: str) -> int:
    slen = len(string)
    if slen == 0:
        return 0

    if slen == 1:
        return 1

    longest = 0
    
    for i in range(slen):
        i_lenght = check_substring(string,i)
        if i_lenght > longest:
            longest = i_lenght

    return longest

def lenght_of_longest_substring_efficient(string: str) ->int:
    slen = len(string)
    if slen == 0:
        return 0

    if slen == 1:
        return 1

    chars = Counter()
    longest = 0
    r = l = 0
    while r < slen:
        r_char = string[r]
        chars[r_char] += 1

        while chars[r_char] > 1:
            l_char = string[l]
            chars[l_char] -= 1
            l += 1
        longest = max(longest, r - l + 1)
        r += 1

    return longest


def duplicates_within_k(numbers, k): 
    '''
    INPUT: list of integers and integer k
    OUTPUT: Boolean indicating whether there is are duplicate elements in the list within k distance
    '''

    if not numbers:
        raise ValueError("The numbers list shouldn't be empty")
    
    if k <= 0:
        raise ValueError("K should be greater than zero")
    
    num_len = len(numbers)
    if num_len == 1:
        return False
    
    if num_len < k:
        k = num_len
    
    repited = {}

    for i in range(num_len):
        if numbers[i] in repited:
            if i - repited[numbers[i]]<= k: #we are in the first subarray
                return True
        else:
            repited[numbers[i]] = i

    return False

    # for indexes in repited.values():
    #     repited_len = len(indexes)
    #     if repited_len > 1: #it is repeated
    #         for i in range(1,repited_len):
    #             if abs(indexes[i]-indexes[i-1]) <= k:
    #                 return True
    
    # for i in range(k):
    #     if repited.get(numbers[i]):
    #         return True
    #     repited[numbers[i]]=True

    # return False
        

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


