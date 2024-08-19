"""
Exercise 1
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
            self.data[self.parent_index(new_node_index)], self.data[new_node_index] = \
                self.data[new_node_index], self.data[self.parent_index(new_node_index)]
            
            # Update the index of the new node:
            new_node_index = self.parent_index(new_node_index)

            
    def has_greater_child(self, index):
        if self.right_child_index(index) == len(self.data):
            if self.data[self.left_child_index(index)] > self.data[index]:
                return True
            else:
                return False
        
        if self.right_child_index(index) < len(self.data) and self.left_child_index(index) < len(self.data):
            if self.data[self.left_child_index(index)] > self.data[index] or self.data[self.right_child_index(index)] > self.data[index]:
                return True
            else:
                return False
        else:
            return False
            
   
    def calculate_larger_child_index(self, index):        
        if self.right_child_index(index) == len(self.data):
            return self.left_child_index(index)
        
        if self.data[self.right_child_index(index)] > self.data[self.left_child_index(index)]:
            return self.right_child_index(index)
        else:
            return self.left_child_index(index)                  
        
        
    def delete(self):
        self.data[0] = self.data.pop()
        trickle_node_index = 0
        
        while self.has_greater_child(trickle_node_index):
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)
            
            self.data[trickle_node_index], self.data[larger_child_index] = \
                self.data[larger_child_index], self.data[trickle_node_index]
                
            trickle_node_index = larger_child_index
 

            
            
if __name__ == '__main__':
    h = Heap()
    
    vals = [10, 9, 8, 6, 5, 7, 4, 2, 1, 3]
    
    for val in vals:
        h.insert(val)
            
    print(h.data)
    
    print()
        
    h.insert(11)
    print(h.data)
    
"""
Returns:

[11, 10, 8, 6, 9, 7, 4, 2, 1, 3, 5]


                        11
                      /   \
                    10     8
                   /  \   / \
                 6    9  7   4
                / \  / \
               2  1 3   5
"""