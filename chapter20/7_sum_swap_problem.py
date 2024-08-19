"""
Recognizing Patterns - The Sum Swap Problem

Algorithm: Pages 413--414 

Time complexity: O(m)
Auxiliary space: O(n)
"""


def sum_swap(array1, array2):
    ht = {} # hash-table to store values of first array
    sum_1 = 0
    sum_2 = 0
    
    # Get sum of first array, while storing its values in the hash-table with index:
    for index, num in enumerate(array1):
        print(f'num = {num}; index = {index}')
        sum_1 += num
        print(f'sum_1 = {sum_1}')
        ht[num] = index # store numbers in hash-table where keys = numbers, values = index
        print(f'ht = {ht}')
        
    # Get sum of second array:
    for n in array2:
        sum_2 += n
        
    # Calculate how much a number in the second array needs to shift by:
    diff = (sum_1 - sum_2) // 2
    print(f'diff = {diff}')
    
    print()
    
    # Iterate over each number in the second array:
    for index, num in enumerate(array2):
        print(f'num = {num}; index = {index}')
        print(f'ht.get(num+diff) = {ht.get(num+diff)}')
        if ht.get(num + diff) is not None:
            return [ht[num + diff], index]
        
    return None
        
    
def sum_swap_v2(array1, array2):
    ht = {i: j for j, i in enumerate(array1)}
    
    sum_1 = sum(array1) # time complexity: O(n)
    sum_2 = sum(array2) # time complexity: O(m)
    
    diff = (sum_1 - sum_2) // 2
    
    for index, num in enumerate(array2):
        if ht.get(num + diff) is not None:
            return [ht[num + diff], index]
        
    return None


if __name__ == '__main__':
    a1 = [1, 2, 3, 4, 5]
    a2 = [6, 7, 8]    
    
    # a1 = [5, 3, 3, 7]
    # a2 = [4, 1, 1, 6]
    
    # a1 = [10, 15, 20]
    # a2 = [5, 30]
    
    res = sum_swap(a1, a2)
    
    print(f'to swap: {a1[res[0]]} in array1 with {a2[res[1]]} in array2' if res is not None else "nothing to swap")
    
