#compare the two list and return another list with the indexes where differences are
from algorithm_practice.arrays_algorithms import concatenate_lists,send_smallest_to_front

newlist = concatenate_lists(["a", "b", "c"], [1, 2, 3])
print(newlist)
newlist = concatenate_lists(None, [1,3])
print(newlist)
newlist = concatenate_lists(5, 4)
print(newlist)

print(send_smallest_to_front([3, 4, 2, 9, 1, 8, 7, 6]))
print(send_smallest_to_front([3, 4, 2, 9, 1, 8, 1, 7, 6]))
