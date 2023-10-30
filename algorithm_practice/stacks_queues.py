class Stack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop(-1)
        
    def add(self, value):
        self.stack.append(value)
        
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

#Create a Queue using two stacks      
class Queue_Om:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.current = self.stack1
        
    def get_other_stack(self):
        if self.current == self.stack1:
            return self.stack2
        
        return self.stack1
        
    def dequeue(self):
        if not self.current:
            return None
        
        value = self.current.pop()
        self.current = self.get_other_stack()
        return value
        
    def enqueue(self, value):
        if not self.current.stack:
            self.current.add(value)
            return
            
        other = self.get_other_stack()
        other_len = len(other.stack)
        curr_len = len(self.current.stack)
        elem_ct = 0
        if other_len < curr_len:
            while other.stack:
                val = other.pop()
                self.current.add(val)
                elem_ct += 1
                
            other.add(value)
            for i in range(elem_ct):
                val = self.current.pop()
                other.add(val)
        else:
            while self.current.stack:
                val = self.current.pop()
                other.add(val)
                elem_ct += 1

            self.current.add(value)
            for i in range(elem_ct):
                val = other.pop()
                self.current.add(val)

class Queue:
    def __init__(self):
        self.data = Stack()
        self.buffer = Stack()

    def dequeue(self):
        if not self.data.stack:
            return None
        
        return self.data.pop()
    
    def enqueue(self, value):
        if not self.data.stack:
            self.data.add(value)
            return
        
        while self.data.stack:
            val = self.data.pop()
            self.buffer.add(val)

        self.data.add(value)

        while self.buffer.stack:
            val = self.buffer.pop()
            self.data.add(val)

class Queue_O:
    def __init__(self):
        self.first_on_top = Stack()
        self.first_on_bottom = Stack()
        
    def dequeue(self):
        if not self.first_on_top.stack and not self.first_on_bottom.stack:
            return None
        
        while self.first_on_bottom.stack:
            val = self.first_on_bottom.pop()
            self.first_on_top.add(val)

        return self.first_on_top.pop()
        
    def enqueue(self, value):
        if not self.first_on_top and not self.first_on_bottom:
            self.first_on_bottom.add(value)
            return
        
        while self.first_on_top.stack:
            val = self.first_on_top.pop()
            self.first_on_bottom.add(val)

        self.first_on_bottom.add(value)

def evalRPN(tokens):
    """
        Evalueate polish 
        :type tokens: List[str]
        :rtype: int
        Input: tokens = ["2","1","+","3","*"]
        Output: 9
        Explanation: ((2 + 1) * 3) = 9
    """
    stack = []
    for elem in tokens:
        if elem == '+':
            stack.append(stack.pop() + stack.pop())
        elif elem == '-':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1-num2)
        elif elem == '*':
            stack.append(stack.pop() * stack.pop())
        elif elem == '/':
            divisor = stack.pop()
            dividend = stack.pop()
            stack.append(int(float(dividend)/divisor))
            
        else:
            stack.append(int(elem))

    return stack[0]