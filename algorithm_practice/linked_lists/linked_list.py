from .node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def add_top(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def get_first(self):
        if not self.head:
            return None
            
        return self.head.val

    def contains(self, value):
        current = self.head

        while current:
            if current.val == value:
                return True
            current = current.next
    
        return False

    def get_at_index(self, index: int):
        if index < 0:
            raise ValueError("Index must be positive")
            
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.val
            current = current.next
            i += 1
        
        return None

    def add_last(self, value):
        current = self.head
        node = Node(value)
        
        if current is not None: 
            while current.next:
                current = current.next
                
            current.next = node
        else:
            self.head = node

    def __repr__(self) -> str:
        current = self.head
        repre = ""

        while current:
            repre += str(current.val) + "-> "
            current = current.next

        return repre

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