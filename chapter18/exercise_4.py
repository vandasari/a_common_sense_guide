"""
Exercise 4
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
        
        
    def bfs_search(self, starting_vertex, search_value):
        queue = []
        visited_vertices = {}        
        visited_vertices[starting_vertex.value] = True
        queue.append(starting_vertex)
        
        while len(queue) > 0:
            current_vertex = queue.pop(0)
            
            if current_vertex.value == search_value:
                return current_vertex.value
            
            for adjacent_vertex in current_vertex.adjacent_vertices:                
                if adjacent_vertex.value not in visited_vertices: 
                    visited_vertices[adjacent_vertex.value] = True
                    queue.append(adjacent_vertex)
            
        return None
    
    
    def bfs_search_steps(self, starting_vertex, search_value):
        print(f'starting_vertex = {starting_vertex.value}')
        queue = []
        visited_vertices = {}        
        visited_vertices[starting_vertex.value] = True
        print(f'visited_vertices = {visited_vertices}')
        queue.append(starting_vertex)
        print(f'queue = {[i.value for i in queue]}')
        
        while len(queue) > 0:
            print(f'len(queue) > 0 = {len(queue)>0}')
            current_vertex = queue.pop(0)
            print(f'current_vertex = {current_vertex.value}; queue = {[i.value for i in queue]}')
            print(f'adjacent_vertices of {current_vertex.value} = {[i.value for i in current_vertex.adjacent_vertices]}')
            
            if current_vertex.value == search_value:
                print(f'current_vertex {current_vertex.value} == search_value {search_value}')
                return current_vertex.value
            
            for adjacent_vertex in current_vertex.adjacent_vertices:
                print(f'adjacent_vertex = {adjacent_vertex.value}')
                
                if adjacent_vertex.value not in visited_vertices: 
                    print(f'{adjacent_vertex.value} is not yet in visited_vertices')
                    visited_vertices[adjacent_vertex.value] = True
                    print(f'visited_vertices = {visited_vertices}')
                    queue.append(adjacent_vertex)
                    print(f'queue = {[i.value for i in queue]}')
            
        return None
        
                        
        
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
        
    toSearch = ['allie', 'drex', 'gina', 'shaun', 'fred']
    n = 2
    
    #--- To show only the result ---#    
    res = alice.bfs_search(alice, toSearch[n])
    print(f'{toSearch[n]} is not found' if res is None else f'{res} is found')
    
    #--- To print/display step-by-step search process: ---#
    # res = alice.bfs_search_steps(alice, toSearch[n])
    # print(f'{toSearch[n]} is not found' if res is None else f'{res} is found')
    
    
"""
                           Alice
                                  
         Bob        Candy        Derek       Elaine
         
         Fred       Helen        Gina
         
                                 Irena

Returns:
    
n = 0 --> allie is not found
n = 2 --> gina is found
"""
