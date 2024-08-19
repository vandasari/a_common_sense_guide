"""
Exercise 4

Write a function that uses a stack to reverse a string. (For example, "abcde" would 
become "edcba".) You can work with our earlier implementation of the Stack class.
"""

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class Stack:
    def __init__(self):
        self.data = [] # Whenever a stack is initiated, we automatically build an empty array with data.
        
    def __len__(self):
        return len(self.data)
    
    def push(self, element):
        self.data.append(element)
    
    def pop(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self.data.pop()
        
    def read(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            raise Empty('Stack is empty')
    
    def isEmpty(self):
        return len(self.data)==0
    
    
def reverse(string):
    
    s = Stack()
    
    for i in string:
        s.push(i)
        
    temp = ''
    while not s.isEmpty():
        temp += s.pop()
        # temp.append(s.pop())
    
    return temp
 
    
if __name__ == '__main__':
    string = 'abcde'
    print(string)
    
    res = reverse(string)
    print(res)