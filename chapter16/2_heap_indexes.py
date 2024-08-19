"""
Algorithm: Page 298
"""

class Heap:
    def __init__(self):
        # Initialize the heap as an empty array:
        self.data = []
        self.first = 0
        self.last = -1
        
    def root_node(self):
        # Returns the first item of the array
        return self.data[self.first]
    
    def last_node(self):
        # Returns the last item of the array
        return self.data[self.last]
    
    def left_child_index(self, index):
        return (index * 2) + 1
    
    def right_child_index(self, index):
        return (index * 2) + 2
    
    def parent_index(self, index):
        return (index - 1) // 2