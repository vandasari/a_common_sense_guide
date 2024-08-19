"""
Exercise 1
"""

def wordBuilder(array):
    collection = []
    
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                collection.append(array[i] + array[j])
    
    return collection
        
   
if __name__ == '__main__':
    arr = ['a', 'b', 'c', 'd']
    
    print(arr) # Original array
    
    print(wordBuilder(arr)) # The resulted array, whose size is now ~ n^2
    
    print(arr) # The original array remain the same.


"""
Time complexity: O(n^2)
Auxiliary space: O(n^2)

Returns:
    
['a', 'b', 'c', 'd']
['ab', 'ac', 'ad', 'ba', 'bc', 'bd', 'ca', 'cb', 'cd', 'da', 'db', 'dc']
['a', 'b', 'c', 'd']
"""
