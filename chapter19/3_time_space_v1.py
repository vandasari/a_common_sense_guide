"""
Trade-Offs Between Time and Space - Version 1

Algorithm: Page 390

Time complexity: O(n^2)
Auxiliary space: O(1)
"""

def hasDuplicateValue(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                return True
            
    return False


if __name__ == '__main__':
    arr = [2, 1, 3, 6, 2, 4, 5]
    print(hasDuplicateValue(arr))
