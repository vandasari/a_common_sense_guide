"""
Queues as Doubly Linked Lists

Algorithm: pages 242--243
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None
        
        
class DoublyLinkedList:        
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node
        
    def insert_at_end(self, value):
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
            
    def remove_from_font(self):
        removed_node = self.first_node
        self.first_node = self.first_node.next_node
        return removed_node
    
    
class Queue:
    def __init__(self):
        self.data = DoublyLinkedList()
        
    def enqueue(self, element):
        self.data.insert_at_end(element)
        
    def dequeue(self):
        removed_node = self.data.remove_from_font()
        return removed_node.data
    
    def read(self):
        if self.data.first_node == None:
            return None
        return self.data.first_node.data

        
        
# Try out:
if __name__ == '__main__':
    q = Queue()
    q.enqueue("once")
    q.enqueue("upon")
    q.enqueue("a")
    q.enqueue("time")
    
    print(q.read())
    
    q.dequeue()
    
    print(q.read())
    
    q.dequeue()
    
    print(q.read())
    
    q.dequeue()
    
    print(q.read())
    
    