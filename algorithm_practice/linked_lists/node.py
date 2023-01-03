class Node:
        
    def __init__(self, value, next=None, prev=None):
        self.value = value 
        # if next is None, this is the last element in the list
        self.next = next
        self.prev = prev

    def __eq__(self, other):
        '''
        Understanding this function is NOT necessary for solving the problem;
        it is only used for the assertions.
        Feel free to explore your curiosity of how this works after the interview :)
        '''
        try:
            return (type(other) == Node and 
                    self.value == other.value and 
                    self.next == other.next)
        except RecursionError:
            raise Exception("Linked list has a cycle or is too large")
