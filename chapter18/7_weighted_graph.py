"""
Weighted Graphs

Algorithm: page 366

Use a hash table to represent the adjacent vertices rather than an array.
"""

class WeightedGraphVertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = {}
        
        
    def add_adjacent_vertex(self, vertex, weight):
        self.adjacent_vertices[vertex] = weight
        
        

if __name__ == '__main__':
    dallas = WeightedGraphVertex('Dallas')
    toronto = WeightedGraphVertex('Toronto')
    boston = WeightedGraphVertex('Boston')
    
    dallas.add_adjacent_vertex(toronto, 138)
    dallas.add_adjacent_vertex(boston, 104)
    toronto.add_adjacent_vertex(dallas, 216)
    
    print(f'Adjacent_vertices of {dallas.value} = {[i.value for i in dallas.adjacent_vertices]}')
    
    print()
    
    for i, j in dallas.adjacent_vertices.items():
        print(f'Flight ticket from {dallas.value} to {i.value} = USD {j}')