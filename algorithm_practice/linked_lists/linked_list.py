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
            
        return self.head.value

    def contains(self, value):
        current = self.head

        while current:
            if current.value == value:
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
                return current.value
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
            repre += str(current.value) + "-> "
            current = current.next

        return repre

    def palindrome(self):
        new_list = LinkedList()
        current = self.head

        while current:
            new_list.add_top(current.value)
            current = current.next

        current = self.head
        current_new_list = new_list.head
        while current and current_new_list:
            if current.value != current_new_list.value:
                return False

            current = current.next
            current_new_list = current_new_list.next

        return True

    def rotate_list(self, k):
        if self.head is None:
            return None

        if k <= 0:
            return self.head

        current = self.head
        lenght = 0
        tail = None
        while current:
            lenght += 1
            if current.next is None:
                tail = current
            current = current.next

        if k >= lenght:
            k = k % lenght

        if k == 0:
            return self.head

        shifted = self.head
        current = shifted.next
        shift = 1
        while current.next:
            if shift == k:
                shifted = shifted.next
            else:
                shift += 1
            current = current.next

        tail.next = self.head
        self.head = shifted.next
        shifted.next = None

        return self.head
    
    def hasCycle(self):
        if not self.head:
            return False

        if not self.head.next:
            return False

        if self.head.next == self.head:
            return True

        slow = self.head
        fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
        

