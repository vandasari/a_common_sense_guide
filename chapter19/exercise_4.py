"""
Exercise 4
"""

def doubleArray_v1(array):
    newArray = []
    
    for i in range(len(array)):
        newArray.append(array[i] * 2)
            
    return newArray


def doubleArray_v2(array):
    for i in range(len(array)):
        array[i] *= 2
        
    return array


def doubleArray_v3(array, index=0):
    if index >= len(array):
        return
    
    array[index] *= 2
    doubleArray_v3(array, index + 1)
    return array
    
        
   
if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    
    # Print original array
    print(arr) 
    
    # The resulted array after reversion, whose size is the same as the variable arr
    print(doubleArray_v3(arr)) 
    
    # If we print again the original array variable and now the array has changed 
    # following the resulted array after reversion, it means auxiliary space O(1),
    # except for recursive method version 3, which is O(n):
    print(arr) 


"""
Version 1:
Time complexity: O(n)
Auxiliary space: O(n)

Version 2:
Time complexity: O(n)
Auxiliary space: O(1)

Version 3:
Time complexity: O(n)
Auxiliary space: O(n)

"""
