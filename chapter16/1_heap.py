"""
Algorithm: Page 297
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