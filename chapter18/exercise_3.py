"""
Exercise 3
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
    
    
    def bfs_traverse(self, starting_vertex):
        queue = []
        visited_vertices = {}        
        visited_vertices[starting_vertex.value] = True
        queue.append(starting_vertex)
        
        while len(queue) > 0:
            # Remove the first vertex off the queue list and make it the current vertex:
            current_vertex = queue.pop(0)
            
            # Iterate over current vertex's adjacent vertices:
            for adjacent_vertex in current_vertex.adjacent_vertices:
                
                if adjacent_vertex.value not in visited_vertices: 
                    visited_vertices[adjacent_vertex.value] = True
                    queue.append(adjacent_vertex)
                    
        return [i for i, j in visited_vertices.items()]
    
    
        
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
    res = a.bfs_traverse(a) 
    print([i for i in res])
    
    
"""
Returns:
    
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
"""
