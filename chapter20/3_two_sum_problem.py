"""
Magical Lookups - The Two-Sum Problem

Algorithm: Page 404

Time complexity: O(n^2)
"""


def twoSum(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] + array[j] == 10:
                return True
            
    return False


if __name__ == '__main__':
    # arr = [2, 0, 4, 1, 7, 9]
    arr = [2, 0, 4, 5, 3, 9]
    
    print(twoSum(arr))