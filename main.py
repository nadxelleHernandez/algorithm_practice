#compare the two list and return another list with the indexes where differences are
from algorithm_practice.arrays_algorithms import (is_palindrome,
      find_nth_element, pairs_with_given_sum)

print(is_palindrome("kayak"))
print(is_palindrome("racecar"))

    

arr = [5, 8, 1, 3, 7, 5, 6]
num = 3
print(find_nth_element(arr, num))

print("Testing sum target")
list = [3,2,8,-1]
sum = 5

result = pairs_with_given_sum(list,sum)
print(f"There are: {result} pairs")
result = pairs_with_given_sum(arr,10)
print(f"There are: {result} pairs")
