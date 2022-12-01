#compare the two list and return another list with the indexes where differences are
from algorithm_practice.my_algorithms import compare_list_same_lenght, concatenate_lists,send_smallest_to_front


list1 = "GAGCCTACTAACGGGAT"
list2 = "CATCGTAATGACGGCCT"

print(compare_list_same_lenght(list1,list2))

example_list = [1, 2, 3, 4, 5, 6]
example_tuple = (1, 2, 3, 4, 5, 6)

print(example_list[0])
print(example_list[-1])
print(example_list[1:4])

print(example_tuple[0])
print(example_tuple[-1])
print(example_tuple[1:4])

newlist = concatenate_lists(["a", "b", "c"], [1, 2, 3])
print(newlist)
newlist = concatenate_lists(None, [1,3])
print(newlist)
newlist = concatenate_lists(5, 4)
print(newlist)

print(send_smallest_to_front([3, 4, 2, 9, 1, 8, 7, 6]))
print(send_smallest_to_front([3, 4, 2, 9, 1, 8, 1, 7, 6]))
