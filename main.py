#compare the two list and return another list with the indexes where differences are
from algorithm_practice.arrays_algorithms import (is_palindrome,
      get_n_largest, pairs_with_given_sum, rotate_list_n2, merge_ordered_lists,in_place_remove)
from algorithm_practice.linked_lists.linked_list import LinkedList
from algorithm_practice.linked_lists.d_linked_list import DLinkedList

# print(is_palindrome("kayak"))
# print(is_palindrome("racecar"))

arr = [5, 8, 1, 3, 7, 6]
start = -1
end   = 0
print(f"In place remove test {arr} start: {start} end: {end}")
print(in_place_remove(arr,start,end))

#num = 3  
# print(f"Rotated list: {rotate_list_n2(arr,num)}")  

# arr = [5, 8, 1, 3, 7, 5, 6, 5]
# num = 5
# n = get_n_largest(arr,num)
# print(f"\n Getting the {num} largest from {arr} is \n {n}")

# print("Testing sum target")
# list = [3,2,8,-1]
# sum = 6

# result = pairs_with_given_sum(list,sum)
# print(f"There are: {result} pairs")
# result = pairs_with_given_sum(arr,num)
# print(f"There are: {result} pairs")

# print("\nTesting merging ordered lists")
# list1 = ['-30', '-10','10']
# list2 = ['0', '1','4','5','11','15']

# result = merge_ordered_lists(list1, list2)

# print(result)

# print("\n Testing palindrome in a Linked list: a, d, a nodes")
# test_list = LinkedList()
# test_list.add_top('a')
# test_list.add_top('d')
# test_list.add_top('a')
# print(test_list.palindrome())

# test_list.add_last('a')

# print("\n Testing palindrome in a Linked list: a, d, a nodes")
# my_list = DLinkedList()
# my_list.add_top('a')
# my_list.add_last('b')
# my_list.add_top('c')


# my_list.add_last('d')


# print(my_list)
# print(my_list.contains_from_head('a'))
# print(my_list.contains_from_tail('i'))

