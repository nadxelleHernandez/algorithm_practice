#compare the two list and return another list with the indexes where differences are
from algorithm_practice.arrays_algorithms import (is_palindrome,
      find_nth_element, pairs_with_given_sum, rotate_list_n2, merge_ordered_lists)

print(is_palindrome("kayak"))
print(is_palindrome("racecar"))

arr = [5, 8, 1, 3, 7, 6]
num = 3  
print(f"Rotated list: {rotate_list_n2(arr,num)}")  

arr = [5, 8, 1, 3, 7, 5, 6, 5]
num = 9
#print(find_nth_element(arr, num))

print("Testing sum target")
list = [3,2,8,-1]
sum = 6

result = pairs_with_given_sum(list,sum)
print(f"There are: {result} pairs")
result = pairs_with_given_sum(arr,num)
print(f"There are: {result} pairs")

print("\nTesting merging ordered lists")
list1 = ['-30', '-10','10']
list2 = ['0', '1','4','5','11','15']

result = merge_ordered_lists(list1, list2)

print(result)
