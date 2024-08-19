"""
Exercise 5
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
        
        
    def find_shortest_path(self, first_vertex, second_vertex, visited_vertices={}):
        queue = []
        
        previous_vertex = {}
        
        visited_vertices[first_vertex.value] = True
        queue.append(first_vertex)
                
        while len(queue) > 0:
            current_vertex = queue.pop(0)
            
            for adjacent_vertex in current_vertex.adjacent_vertices:
                if adjacent_vertex.value not in visited_vertices:
                    visited_vertices[adjacent_vertex.value] = True
                    queue.append(adjacent_vertex)                    
                    previous_vertex[adjacent_vertex.value] = current_vertex.value
        
        shortest_path = []
        
        current_vertex_value = second_vertex.value
        
        while current_vertex_value != first_vertex.value:
            shortest_path.append(current_vertex_value)
            current_vertex_value = previous_vertex[current_vertex_value]
            
        shortest_path.append(first_vertex.value)
        
        return shortest_path[::-1]
    
    
    def find_shortest_path_steps(self, first_vertex, second_vertex, visited_vertices={}):
        queue = []
        
        previous_vertex = {}
        
        visited_vertices[first_vertex.value] = True
        queue.append(first_vertex)
        print(f'visited_vertices = {visited_vertices}')
        print(f'queue = {[i.value for i in queue]}')
        
        
        while len(queue) > 0:
            current_vertex = queue.pop(0)
            print(f'current_vertex = {current_vertex.value}, queue = {[i.value for i in queue]}')
            
            print(f'adjacent_vertices of {current_vertex.value} = {[i.value for i in current_vertex.adjacent_vertices]}')
            for adjacent_vertex in current_vertex.adjacent_vertices:
                print(f'adjacent_vertex = {adjacent_vertex.value}')
                if adjacent_vertex.value not in visited_vertices:
                    print(f'{adjacent_vertex.value} not in visited_vertices')
                    visited_vertices[adjacent_vertex.value] = True
                    print(f'visited_vertices = {visited_vertices}')
                    queue.append(adjacent_vertex)
                    print(f'queue = {[i.value for i in queue]}')
                    
                    previous_vertex[adjacent_vertex.value] = current_vertex.value
                    print(f'previous_vertex = {previous_vertex}')
        
        shortest_path = []
        
        current_vertex_value = second_vertex.value
        print(f'current_vertex_value = {current_vertex_value} - before looping')
        
        while current_vertex_value != first_vertex.value:
            print(f'{current_vertex_value} != {first_vertex.value} = {current_vertex_value != first_vertex.value}')
            shortest_path.append(current_vertex_value)
            current_vertex_value = previous_vertex[current_vertex_value]
            print(f'current_vertex_value = {current_vertex_value}')
            
        shortest_path.append(first_vertex.value)
        print(f'shortest_path = {shortest_path[::-1]}')

        
        
if __name__ == '__main__':
    idris = Vertex('Idris')
    kamil = Vertex('Kamil')
    talia = Vertex('Talia')
    lina = Vertex('Lina')
    ken = Vertex('Ken')
    marco = Vertex('Marco')
    sasha = Vertex('Sasha')
    
    idris.add_adjacent_vertex_undirected(kamil)
    idris.add_adjacent_vertex_undirected(talia)
    kamil.add_adjacent_vertex_undirected(lina)
    talia.add_adjacent_vertex_undirected(ken)
    ken.add_adjacent_vertex_undirected(marco)
    marco.add_adjacent_vertex_undirected(sasha)
    sasha.add_adjacent_vertex_undirected(lina)
                
    
    #--- To show only the result ---#    
    # res = idris.find_shortest_path(idris, lina)
    # print(res)
    
    #--- To print/display step-by-step search process: ---#
    idris.find_shortest_path_steps(idris, lina)
    
"""
Returns:
    
['Idris', 'Kamil', 'Lina']
"""
    