"""
Algorithm: page 165
"""

def double_array(array, index=0):
    # base case, when the index goes past the end of the array
    if index >= len(array):
        return
    
    array[index] *= 2
    return double_array(array, index + 1)
    
    
if __name__ == '__main__':
    arr = [1, 2, 3, 4] 
    double_array(arr) 
    print(arr)