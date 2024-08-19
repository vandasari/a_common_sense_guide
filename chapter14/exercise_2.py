"""
Exercise 2

Add a method to the DoublyLinkedList class that prints all the elements of 
the list in reverse order.
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
        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        # If the linked list already has at least one node:
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node
            
    def print_reverse(self, ended=None):
        current_node = self.last_node.data
        
        while current_node:
            print(current_node.data, end=ended)
            current_node = current_node.previous_node
 
            
if __name__ == '__main__':            
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")
    
    node_4.previous_node = node_3
    node_3.previous_node = node_2
    node_2.previous_node = node_1
    
    d = DoublyLinkedList()
    d.insert(node_1)
    d.insert(node_2)
    d.insert(node_3)
    d.insert(node_4)
    
    d.print_reverse(ended=' ')
    
    