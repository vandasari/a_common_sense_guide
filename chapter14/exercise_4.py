"""
Exercise 4

Here’s a tricky one. Add a method to the classic LinkedList class that reverses 
the list. That is, if the original list is A -> B -> C, all of the list’s links 
should change so that C -> B -> A.
"""

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
        
      
class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node
        # self.size = 0
        
    # def __len__(self):
    #     return self.size
 
        
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
            return # end the method early, as there’s nothing left to do
        
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
        
        
    def delete(self, index):
        # If we are deleting the first node:
        if index == 0:
            # Simply set the current 2nd node (the next of the current 1st node) 
            # to be the 1st node: 
            self.first_node = self.first_node.next_node
            return # end the method
        
        # If we are deleting anywhere other than the beginning:
        current_node = self.first_node
        current_index = 0
        
        # First, we find the node immediately before the one we wan to delete
        # and call it current node:
        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1
            
        # We find the node that comes after the one we're deleting:
        node_after_deleted_node = current_node.next_node.next_node
        
        # We change the link of the curernt_node to point to the node_after_deleted_node,
        # leaving the node we want to delete out of the list:
        current_node.next_node = node_after_deleted_node
        
        
    def printall(self, ended=None):
        current_node = self.first_node
        
        while current_node:
            print(current_node.data, end=ended)
            current_node = current_node.next_node
            
            
    def read_last(self):
        current_node = self.first_node
                
        while current_node:
            # If we reach the last element, return the data:
            if current_node.next_node == None:
                return current_node.data
            current_node = current_node.next_node
            
        return None
    
    
    def reverse(self):
        p_node = None
        current_node = self.first_node
        
        while current_node:
            n_node = current_node.next_node
            current_node.next_node = p_node
            p_node = current_node
            current_node = n_node
            
        self.first_node = p_node
 


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
    
    # Set the 1st element as the head of chain:
    alist = LinkedList(node_1)
        
    # Exercise 1: To print all elements of the list:
    alist.printall(ended=' ')
   
    print('\n')
   
    # Exercise 3: Return the last element:
    print(f'The last element: {alist.read_last()}')
    
    print()
    
    # Exercise 4: Reverse the list
    alist.reverse()
    
    # Print all elements of the reversed list:
    alist.printall(ended=' ')
    
 
