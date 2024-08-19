"""
Algorithm: page 101
Time complexity: O(n)

The code contains 2 loops:
    - an outer loop that revolves around n times
    - an inner loop that runs a constant 5 times
    
While the outer loop runs n times, the inner loop runs 5 times for each of the
n array (clothing_items). This means this algorithm runs 5n times, but its
time complexity is reduced to O(n).
"""

def mark_inventory(clothing_items):
    clothing_options = []
    
    for item in clothing_items: # outer loop revolves around n times
        # For sizes 1 through 5
        for size in range(1, 6): # this inner loop runs a constant 5 times
            clothing_options.append(item + " Size: " + str(size))
            
    return clothing_options


if __name__ == '__main__':
    a = ['Green T-Shirt', 'Red Trousers', 'Blue Top']
    
    res = mark_inventory(a)
    
    print(res)

"""
Returns:

['Green T-Shirt Size: 1', 
 'Green T-Shirt Size: 2', 
 'Green T-Shirt Size: 3', 
 'Green T-Shirt Size: 4', 
 'Green T-Shirt Size: 5', 
 'Red Trousers Size: 1', 
 'Red Trousers Size: 2', 
 'Red Trousers Size: 3', 
 'Red Trousers Size: 4', 
 'Red Trousers Size: 5', 
 'Blue Top Size: 1', 
 'Blue Top Size: 2', 
 'Blue Top Size: 3', 
 'Blue Top Size: 4', 
 'Blue Top Size: 5']
"""