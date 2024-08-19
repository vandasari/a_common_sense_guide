"""
Chapter: 13 Recursive Algorithms for Speed
Exercise: 2
Page: 224

The following function finds the “missing number” from an array of integers. 
That is, the array is expected to have all integers from 0 up to the array’s 
length, but one is missing. As examples, the array, [5, 2, 4, 1, 0] is missing 
the number 3, and the array, [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the number 8.
Use sorting to write a new implementation of this function that only 
takes O(n log(n)). 
"""

# Time complexity: O(n^2)
def findMissingNumberQuestion(array):
    for i in range(len(array)): # n steps
        if i not in array: # n steps 
            return i
        
    return None


# Time complexity: O(n log(n))
def findMissingNumberSolution(array):
    array = sorted(array)
    
    for i in range(len(array)):
        if i != array[i]:
            return i
        
    return None


if __name__ == '__main__':
    arr = [5, 2, 4, 1, 0]
    # arr = [9, 3, 2, 5, 6, 7, 1, 0, 4]
    res = findMissingNumberSolution(arr)
    
    
    if res is None:
        print('All numbers are present')
    else:
        print(f'Missing number(s): {res}')
    
    

