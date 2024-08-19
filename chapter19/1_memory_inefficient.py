"""
Big O of Space Complexity

Algorithm: Page 388

Auxiliary space: O(n)
Time complexity: O(n)
"""

def makeUpperCase(array):
    newArray = []
    
    for i in array:
        newArray.append(i.upper())
        
    return newArray



if __name__ == '__main__':
    arr = ['tuvi', 'leah', 'shaya', 'rami']
    print(arr)
    print(makeUpperCase(arr))
    print(arr)