from .node import Node

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add_top(self, value):
        new_node = Node(value)
        if self.head: #there is a head already
            self.head.prev = new_node
            new_node.next = self.head
        else:  #its the first element to add
            self.tail = new_node
        
        self.head = new_node
        self.len += 1

    def get_first(self):
        if not self.head:
            return None
            
        return self.head.val

    def contains_from_head(self, value):
        current = self.head

        while current:
            if current.val == value:
                return True
            current = current.next
    
        return False

    def contains_from_tail(self, value):
        current = self.tail

        while current:
            if current.val == value:
                return True
            current = current.prev
    
        return False

    def get_at_index(self, index: int):
        if index >= 0:    
            current = self.head
            i = 0
            while current:
                if i == index:
                    return current.val
                current = current.next
                i += 1
        else:
            index = abs(index)
            current = self.tail
            i = 0
            while current:
                if i == index:
                    return current.val
                current = current.prev
                i += 1

        return None

    def add_last(self, value):
        node = Node(value)
        
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        else: #its the first element
            self.head = node
        
        self.tail = node
        self.len += 1

    def __repr__(self) -> str:
        current = self.head
        repre = ""

        while current:
            repre += str(current.val) + "<-> "
            current = current.next

        return repre