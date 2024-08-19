"""
Algorithm: Page 298--299
Time complexity: O(log n)
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
    
    def insert(self, value):
        # Turn value into last node by inserting it at the end of the array:
        self.data.append(value)
        
        # Keep track of the index of the newly inserted node
        new_node_index = len(self.data) - 1
        
        # The following loop executes the "trickle up" algorithm.
        # If the new node is not in the root position, and it's greater than its parent node:
        while new_node_index > 0 and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]:
            # Swap the new node with the parent node:
            self.data[self.parent_index(new_node_index)], self.data[new_node_index] = self.data[new_node_index], self.data[self.parent_index(new_node_index)]
            
            # Update the index of the new node:
            new_node_index = self.parent_index(new_node_index)
            
            
if __name__ == '__main__':
    h = Heap()
    h.insert(100)
    h.insert(88)
    h.insert(25)
    h.insert(87)
    h.insert(16)
    
    
    print(h.data)
    print(h.root_node())
    print(h.last_node())
    
    
"""
               100
               / \
             88  25
            / \
          87  16
"""