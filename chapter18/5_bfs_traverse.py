"""
Breadth-First Search (BFS) Traversal

Algorithm: Page 358
Time complexity: O(v+e), where v = number of vertices and e = number of edges

Implementation of breadth-first search traversal using a list instead of Queue.
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
        # Mark vertex as visited by adding it to the hash table:
        visited_vertices[vertex.value] = True
        
        # print(vertex.value)
        
        # Iterate through the current vertex's adjacent vertices:
        for adjacent_vertex in vertex.adjacent_vertices:
            # If the adjacent vertex is not in the hash table of visited vertices:
            if adjacent_vertex.value not in visited_vertices:
                # Recursively call this method on the adjacent vertex:
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
            
        # return visited_vertices
        
        
    def dfs_seaarch(self, vertex, search_value, visited_vertices={}):
        # Return the original vertex if it happens to be the one we're searching for:
        if vertex.value == search_value:
            return vertex
        
        visited_vertices[vertex.value] = True
        
        for adjacent_vertex in vertex.adjacent_vertices:
            if adjacent_vertex.value not in visited_vertices:
                if adjacent_vertex.value == search_value:
                    return adjacent_vertex
                
                # Attempt to find the vertex we're searching for by recursively
                # calling this method on the adjacent vertex:
                sought_vertex = self.dfs_seaarch(adjacent_vertex, search_value, visited_vertices)
                
                # If we were able to find the correct vertex using the above 
                # recursion, return the correct vertex:
                if sought_vertex:
                    return sought_vertex
        
        # If we weren't able to find the vertex we're searching for:
        return None
    
    
    def dfs_search_steps(self, vertex, search_value, visited_vertices={}):
        print(f'current vertex = {vertex.value}')
        if vertex.value == search_value:
            print(f'current vertex {vertex.value} == search_value {search_value}')
            return vertex
        
        visited_vertices[vertex.value] = True
        print(f'visited_vertices = {visited_vertices}')
        
        print(f'adjacent_vertices of {vertex.value} = {[i.value for i in vertex.adjacent_vertices]}')
        
        for adjacent_vertex in vertex.adjacent_vertices:
            print(f'adjacent_vertex = {adjacent_vertex.value}')
            if adjacent_vertex.value not in visited_vertices:
                print(f'{adjacent_vertex.value} is not yet in visited_vertices')
                if adjacent_vertex.value == search_value:
                    print(f'{adjacent_vertex.value} is the search_value')
                    return adjacent_vertex
                
                sought_vertex = self.dfs_search_steps(adjacent_vertex, search_value, visited_vertices)
                print('vertex not found' if sought_vertex is None else 'vertex is found')
                
                if sought_vertex:
                    print(f"vertex we're looking for is {sought_vertex.value}")
                    return sought_vertex
        
        return None
    
    
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
    
    
    def bfs_traverse_steps(self, starting_vertex):
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
            
            for adjacent_vertex in current_vertex.adjacent_vertices:
                print(f'adjacent_vertex = {adjacent_vertex.value}')
                
                if adjacent_vertex.value not in visited_vertices: 
                    print(f'{adjacent_vertex.value} is not yet in visited_vertices')
                    visited_vertices[adjacent_vertex.value] = True
                    print(f'visited_vertices = {visited_vertices}')
                    queue.append(adjacent_vertex)
                    print(f'queue = {[i.value for i in queue]}')
                    
        print([i for i, j in visited_vertices.items()])
                        
        
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
        
    
           
    #--- To show only the result ---#
    res = alice.bfs_traverse(alice)
    print(res)
    
    #--- To print/display step-by-step search process: ---#
    # alice.bfs_traverse_steps(alice)
    
    
"""
                           Alice
                                  
         Bob        Candy        Derek       Elaine
         
         Fred       Helen        Gina
         
                                 Irena

Returns:
    
['alice', 'bob', 'candy', 'derek', 'elaine', 'fred', 'helen', 'gina', 'irena']
"""
