"""
Implementing a Linked List

Algorithm: Page 228

With this example of linked list class, we only have immediate access to its first node.
"""

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
        
      
class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node
         
        
if __name__ == '__main__':
    # Create a chain/list of 4 nodes containing strings:        
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")
    
    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4
    
    # Create an instance of LinkedList that has access to the list's 1st node:
    alist = LinkedList(node_1)
    
    # Print the first node of linked list:
    print(alist.first_node.data)
    
