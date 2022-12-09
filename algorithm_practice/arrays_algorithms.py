from collections.abc import Iterable  

'''
Given two arrays, create your own concatenation function. Return a new array containing the first array's values, then the second array's values. Try not to use built-in methods.  Don't forget edge cases!

Example Input: ["a", "b", "c"], [1, 2, 3]
Example Output: ["a", "b", "c", 1, 2, 3]
'''
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

'''
Given an array, find the smallest value and move it to the front of the array. Return the same array. Try not to use built-in methods. Don't forget edge cases!

Example Input: [3, 4, 2, 9, 1, 8, 7, 6]
Example Output: [1, 3, 4, 2, 9, 8, 7, 6]

Example Input: [3, 4, 2, 9, 1, 8, 1, 7, 6]
Example Output: [1, 3, 4, 2, 9, 8, 1, 7, 6]

'''
def send_smallest_to_front(lst):
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
    
'''
Given an array, reverse the order of values without using the built-in method reverse or slice, 
ie. [: :-1]. Return the same array. Don't forget edge cases!

Example Input: [1, 2, 3, 4, 5, 6]
Example Output: [6, 5, 4, 3, 2, 1]
'''
def reverse_list(lst):
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
  for i in range(shift_by):
    list.insert(0, list.pop(-1))
  return list
'''
def rotate_list(lst, shift_by):
    pass

'''
Write a function that determine if a string is a palindrome
Don't accept numbers type (raise exception)
Accept iterables
trim spaces at the ends
Accepts special characters (in case we have a frase)
'''
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
    if string is None or not iterable(string):
        raise ValueError("is_palindrome received an empty or non iterable argument")

    if not string: 
        return False

    if type(str) is not str:
        work_str = convert_list_to_string(string)
    else:
        work_str = string

    str_len = len(work_str)
    for i in range(str_len//2):
        if work_str[i].upper() != work_str[str_len-i-1].upper():
            return False

    return True

def get_n_largest(list, n):
    list.sort()
    #print(list)
    #lists = []
    #for num in list:
    # if num not in lists:
        #  lists.append(num)
    if len(list) < n:
        return None
    return list[-n]

def in_place_remove(list, start, end):
    removes = (end - start) + 1
    while removes > 0:
        list.pop(start)
        removes -= 1
    return list

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

'''Create a function named pairs_with_given_sum 
It finds the number of pairs of numbers in a list which add up to a given target. 
This function should take in a list of whole numbers and a target as parameters. 
This function should have a return value of the integer of number of pairs.
numbers:	[1, 2, 4, 5]  
target: 6	
Number of pairs (return value) : 2
'''
def pairs_with_given_sum(lst, target_sum):
    if not lst:
        return 0

    helper = dict()
    for num in lst:
        helper[num] = False

    pairs = 0
    for key in helper.keys():
        other_pair_key = target_sum - key
        other_pair_val = helper.get(other_pair_key)
        if other_pair_val is not None and other_pair_val == False:
            pairs += 1
            helper[key] = True
            helper[other_pair_key] = True

    return pairs

