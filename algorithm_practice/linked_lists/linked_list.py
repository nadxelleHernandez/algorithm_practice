from .node import Node

class LinkedList:
    def __init__(self):
        self.head = None
      
    def add_top(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def palindrome(self):
      new_list = LinkedList()
      current = self.head

      while current:
        new_list.add_top(current.val)
        current = current.next

      current = self.head
      current_new_list = new_list.head
      while current and current_new_list:
        if current.val != current_new_list.val:
          return False

        current = current.next
        current_new_list = current_new_list.next

      return True