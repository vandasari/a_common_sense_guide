"""
Trade-Offs Between Time and Space - Version 2

Algorithm: Page 390

Time complexity: O(n)
Auxiliary space: O(n)
"""

def hasDuplicateValue(array):
    existingValues = {} # the hash table creates a new space
    
    for i in range(len(array)):
        if array[i] not in existingValues:
            existingValues[array[i]] = True
        else:
            return True
            
    return False


if __name__ == '__main__':
    arr = [2, 1, 3, 6, 2, 4, 5]
    print(hasDuplicateValue(arr))
