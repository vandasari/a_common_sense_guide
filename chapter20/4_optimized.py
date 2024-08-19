"""
Magical Lookups - Optimized The Two Sum Problem with The Hash Table

Algorithm: Page 405--406

Time complexity: O(n)
"""


def twoSum(array):
    
    hash_table = {}
    
    for i in range(len(array)):
        if hash_table.get(10 - array[i]):
            return True        
        hash_table[array[i]] = True

    return False


if __name__ == '__main__':
    arr = [2, 0, 4, 1, 7, 9]
    # arr = [2, 0, 4, 5, 3, 9]
    
    print(twoSum(arr))
    