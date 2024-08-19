"""
Exercise 5 

Time complexity: O(n)
"""


def sortTemperatures(array):
    ht = {}
    
    # Populate hash table with occurrences of temperatures:
    for t in array:
        if ht.get(t) is not None:
            ht[t] += 1
        else:
            ht[t] = 1
            
    sortedArray = []
    
    temperature = 970
    
    while temperature <= 990:
        if ht.get(temperature / 10.0) is not None:
            m = ht.get(temperature / 10.0)
            for times in range(m):
                sortedArray.append(temperature/10.0)
        
        temperature += 1
    
    return sortedArray



if __name__ == '__main__':
    
    arr = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]
    
    print(sortTemperatures(arr))
    

"""
Returns:
    
[97.1, 97.1, 97.8, 98.0, 98.0, 98.2, 98.5, 98.6, 98.9, 99.0]
"""