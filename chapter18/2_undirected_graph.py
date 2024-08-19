"""
Object-Oriented Graph Implementation - Undirected Graph

Algorithm: Page 336

Implementation of a graph using a simple list (in the form of an array) to store
a vertex's adjacent vertices.
"""

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []
        
        
    # For directed graph
    def add_adjacent_vertex_directed(self, vertex):
        # The adjacent_vertices array contains all the vertices a vertex connects to:
        self.adjacent_vertices.append(vertex)
        
    
    # For undirected graph
    def add_adjacent_vertex_undirected(self, vertex):
        # If a vertex is alreaady in the adjcent_vertices, do nothing:
        if vertex in self.adjacent_vertices:
            return
        
        # Otherwise, add the vertex into the adjacent_vertices list (add Bob to Alice's list):
        self.adjacent_vertices.append(vertex)
        
        # This is for going the other way (add Alice to Bob's list):
        vertex.add_adjacent_vertex_undirected(self)
        
        
        
if __name__ == '__main__':
    alice = Vertex('alice')
    bob = Vertex('bob')
    cynthia = Vertex('cynthia')
    
    alice.add_adjacent_vertex_undirected(bob)
    alice.add_adjacent_vertex_undirected(cynthia)
    bob.add_adjacent_vertex_undirected(cynthia)
    
    # Get Bob's friends:
    for i in bob.adjacent_vertices:
        print(i.value)
        
        
"""
Returns:
    
alice
cynthia
"""