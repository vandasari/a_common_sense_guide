"""
Insertion

Algorithm: Pages 234--235
Time complexity: O(1) for insertion at the beginning of the list 
                 O(n) for insertion at the end of the list
"""

import timeit


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
        
      
class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node
 
        
    def read(self, index):
        current_node = self.first_node
        current_index = 0
        
        while current_index < index:
            # Access the next node in the list and make it the new current node:
            current_node = current_node.next_node
            current_index += 1
            
            # If we're past the end of the list, that means the value cannot be
            # found in the list, so return None:
            if not current_node:
                return None
            
        return current_node.data
    
    
    def search(self, value):
        current_node = self.first_node
        current_index = 0
        
        while current_node:
            if current_node.data == value:
                return current_index
            
            current_node = current_node.next_node
            current_index += 1
            
            if not current_node:
                return None
        
    
    def insert(self, index, value):
        # Create a new node with the provided value:
        new_node = Node(value)
        
        # If we are inserting at the beginning of the list:
        if index == 0:
            # Our new_node now links to the first node of the list:
            new_node.next_node = self.first_node
            # Declare that our new_node is now the list's first node going forward:
            self.first_node = new_node
            return # ends the method early, as there’s nothing left to do
        
        # If we are inserting anywhere other than the beginning:
        current_node = self.first_node
        current_index = 0
        
        # First, we access the node immediately before where the new node will go:
        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1
            
        # We set the link of our new_node to point the node after the current_node:
        new_node.next_node = current_node.next_node
        
        # Modify the link of the previous node to point to our new node:
        current_node.next_node = new_node


if __name__ == '__main__':
    # Create data:         
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")
    
    # Create a chain of nodes from the data:
    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4
    
    # Set the 1st node as the head of chain:
    alist = LinkedList(node_1)
    
    # To read the 4th node from the list:
    print(alist.read(3))
    
    # To search for any value within the list:
    print(alist.search("upon"))
    print(alist.search("time"))
    
    # To insert "purple" at index 3:
    alist.insert(3, "purple")
    
    # Read all 5 nodes from the list:
    for i in range(5):
        print(alist.read(i), end=' ')
        
    print()
    
    # Search the value of "time" again, whose index has now changed:
    print(alist.search("time"))
    
    print()
    
    # Benchmarking for insertion at beginning
    print(f'alist = {[alist.read(i) for i in range(5)]}')   
    print('Linked List:', timeit.timeit('[func(0, "some") for func in (alist.insert, )]', globals=globals(), number=1), 'sec')
    print(f'alist = {[alist.read(i) for i in range(6)]}')
    
    print()
    
    arr = [2, 3, 4, 5, 6]
    
    print(f'arr = {arr}')   
    print('Array:', timeit.timeit('[func(0, 8) for func in (arr.insert, )]', globals=globals(), number=1), 'sec')
    print(f'arr = {arr}')
