"""
Doubly Linked Lists

Algorithm: page 240
Time complexity: O(1)
"""

class Node:
    def __init__(self, data, next_node=None, previous_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node
        
        
class DoublyLinkedList:
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node
        
    def insert(self, value):
        # Create a new node:
        new_node = Node(value)
        
        # If there are no elements yet in the linked list:
        if self.first_node == None:
            self.first_node = new_node
            self.last_node = new_node
        # If the linked list already has at least one node:
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node
 
            
if __name__ == '__main__':            
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")
    
    d = DoublyLinkedList()
    d.insert(node_1)
    d.insert(node_2)
    d.insert(node_3)
    res = d.insert(node_4)
    
    # Accessing the node items:
    print(d.first_node.data.data)
    print(d.first_node.next_node.data.data)
    print(d.first_node.next_node.next_node.data.data)
    print(d.first_node.next_node.next_node.next_node.data.data)
    
    print()
    
    print(d.last_node.data.data)
    print(d.last_node.previous_node.data.data)
    print(d.last_node.previous_node.previous_node.data.data)
    print(d.last_node.previous_node.previous_node.previous_node.data.data)
    