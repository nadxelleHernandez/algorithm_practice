from collections.abc import Iterable  

'''
Compare the two list of the same lenght and return another list 
with the indexes where differences are
'''
def compare_list_same_lenght(list_1,list_2):
    if len(list_1)!= len(list_2) :
        return None

    diffence = list()
    i = 0
    for elem in list_1:
        if elem != list_2[i]:
            diffence.append(i)
        i+=1

    return diffence

'''
Given two arrays, create your own concatenation function. Return a new array containing the first array's values, then the second array's values. Try not to use built-in methods.  Don't forget edge cases!

Example Input: ["a", "b", "c"], [1, 2, 3]
Example Output: ["a", "b", "c", 1, 2, 3]
'''
def iterable(obj):
    return isinstance(obj,Iterable)

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
    