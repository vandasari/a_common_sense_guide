"""
Depth-First Search

Algorithm: Page 347
Time complexity: O(v+e), where v = number of vertices and e = number of edges

Implementation of depth-first traversal.
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
        if vertex in self.adjacent_vertices:
            return
        
        # The adjacent_vertices array contains all the vertices a vertex connects to:
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex_undirected(self)
        
        
    def dfs_traverse(self, vertex, visited_vertices={}):
        visited_vertices[vertex.value] = True
                
        for adjacent_vertex in vertex.adjacent_vertices:
            if adjacent_vertex.value not in visited_vertices:
                self.dfs_traverse(adjacent_vertex, visited_vertices)
            
        return visited_vertices
    
    
    def dfs_traverse_steps(self, vertex, visited_vertices={}):
        print(f'current vertex = {vertex.value}')
        visited_vertices[vertex.value] = True
        print(f'visited_vertices = {visited_vertices}')
        
        # print(vertex.value)
        print(f'adjacent_vertices of {vertex.value} = {[i.value for i in vertex.adjacent_vertices]}')
        
        for adjacent_vertex in vertex.adjacent_vertices:
            print(f'adjacent_vertex = {adjacent_vertex.value}')
            if adjacent_vertex.value not in visited_vertices:
                print(f'{adjacent_vertex.value} is not yet in visited_vertices')
                self.dfs_traverse_steps(adjacent_vertex, visited_vertices)
            else:
                print(f'{adjacent_vertex.value} is already in visited_vertices')
           
        print([i for i in visited_vertices])
        
        
if __name__ == '__main__':
    alice = Vertex('alice')
    bob = Vertex('bob')
    candy = Vertex('candy')
    derek = Vertex('derek')
    elaine = Vertex('elaine')
    fred = Vertex('fred')
    gina = Vertex('gina')
    helen = Vertex('helen')
    irena = Vertex('irena')
    
    alice.add_adjacent_vertex_undirected(bob)
    bob.add_adjacent_vertex_undirected(fred)
    fred.add_adjacent_vertex_undirected(helen)
    helen.add_adjacent_vertex_undirected(candy)
    candy.add_adjacent_vertex_undirected(alice)
        
    alice.add_adjacent_vertex_undirected(derek)
    derek.add_adjacent_vertex_undirected(gina)
    gina.add_adjacent_vertex_undirected(irena)
    
    alice.add_adjacent_vertex_undirected(elaine)
    elaine.add_adjacent_vertex_undirected(derek)                
    
    #-- Results --#
    res = alice.dfs_traverse(alice) 
    print([i for i in res])
    
    #-- Display step-by-step DFS traversal --#
    # alice.dfs_traverse_steps(alice)


"""
                          Alice
                                 
        Bob        Candy        Derek       Elaine
        
        Fred                    Gina
        
       Helen                    Irena

Returns:

alice
bob
fred
helen
candy
derek
gina
irena
elaine
"""