"""
Linked List Search

Algorithm: Page 231
Time complexity: O(n)
"""

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
        # We begin at the first node of the list:
        current_node = self.first_node
        current_index = 0
        
        while current_node:
            # If we find the data we're looking for, we return it:
            if current_node.data == value:
                return current_index
            
            # Otherwise, we move on to the next node:
            current_node = current_node.next_node
            current_index += 1
            
        if not current_node:
            return None
        

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


"""
The mechanics of searching are similar to reading. The main difference is that 
the loop doesn’t stop at a particular index, but runs until we either find the 
value or reach the end of the list.
"""