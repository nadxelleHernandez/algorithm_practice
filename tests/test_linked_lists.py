from algorithm_practice.linked_lists.linked_list import LinkedList
from algorithm_practice.linked_lists.node import Node

def test_has_cycle_list_with_no_cycle():
    list = LinkedList()
    list.add_last(3)
    list.add_last(2)
    list.add_last(0)
    list.add_last(-4)

    assert list.hasCycle() == False  
