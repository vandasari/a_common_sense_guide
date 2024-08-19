"""
Big O of Space Complexity

Algorithm: Page 389

Auxiliary space: O(1)
Time complexity: O(n)
"""

def makeUpperCase(array):
        
    for i in range(len(array)):
        array[i] = array[i].upper()
        
    return array


if __name__ == '__main__':
    arr = ['tuvi', 'leah', 'shaya', 'rami']
    print(arr)
    print(makeUpperCase(arr))
    print(arr)

# Or, we can also use list comprehension in Python:

# arr = [i.upper() for i in arr]
# print(arr)