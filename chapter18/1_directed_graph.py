"""
Object-Oriented Graph Implementation - Directed Graph

Algorithm: Page 335

Implementation of a graph using a simple list (in the form of an array) to store
a vertex's adjacent vertices.
"""

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []
        
        
    # For directed graph
    def add_adjacent_vertex(self, vertex):
        # The adjacent_vertices array contains all the vertices a vertex connects to:
        self.adjacent_vertices.append(vertex)
        
        
        
if __name__ == '__main__':
    alice = Vertex('alice')
    bob = Vertex('bob')
    cynthia = Vertex('cynthia')
    
    alice.add_adjacent_vertex(bob)
    alice.add_adjacent_vertex(cynthia)
    bob.add_adjacent_vertex(cynthia)
    cynthia.add_adjacent_vertex(bob)
    
    # Get friends that Bob follows:
    for b in bob.adjacent_vertices:
        print(b.value)
        
    print()
        
    # Get friends that Alice follows:
    for a in alice.adjacent_vertices:
        print(a.value)
        
        
"""
Returns:
    
cynthia

bob
cynthia
"""