"""
Exercise 2
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
    
        
        
if __name__ == '__main__':
    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    e = Vertex('E')
    f = Vertex('F')
    g = Vertex('G')
    h = Vertex('H')
    i = Vertex('I')
    j = Vertex('J')
    k = Vertex('K')
    l = Vertex('L')
    m = Vertex('M')
    n = Vertex('N')
    o = Vertex('O')
    p = Vertex('P')
    
    a.add_adjacent_vertex_undirected(b)
    a.add_adjacent_vertex_undirected(c)        
    a.add_adjacent_vertex_undirected(d)    
    b.add_adjacent_vertex_undirected(e)
    b.add_adjacent_vertex_undirected(f)    
    c.add_adjacent_vertex_undirected(g)       
    d.add_adjacent_vertex_undirected(h)
    d.add_adjacent_vertex_undirected(i)        
    e.add_adjacent_vertex_undirected(j)    
    f.add_adjacent_vertex_undirected(j)
    g.add_adjacent_vertex_undirected(k)
    h.add_adjacent_vertex_undirected(l)
    h.add_adjacent_vertex_undirected(m)
    i.add_adjacent_vertex_undirected(m)
    i.add_adjacent_vertex_undirected(n)
    j.add_adjacent_vertex_undirected(o)
    n.add_adjacent_vertex_undirected(p)
                 
    
    #-- Results --#
    res = a.dfs_traverse(a) 
    print([i for i in res])

"""


Returns:

['A', 'B', 'E', 'J', 'F', 'O', 'C', 'G', 'K', 'D', 'H', 'L', 'M', 'I', 'N', 'P']
"""