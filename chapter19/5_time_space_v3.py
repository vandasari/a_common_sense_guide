"""
Trade-Offs Between Time and Space - Version 3

Algorithm: Page 391

Time complexity: O(n log n)
Auxiliary space: O(log n)
"""

def hasDuplicateValue(array):
    array = sorted(array) # Tim's sort: O(n log n)
    
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            return True
            
    return False


if __name__ == '__main__':
    arr = [2, 1, 3, 6, 2, 4, 5]
    print(hasDuplicateValue(arr))
    

