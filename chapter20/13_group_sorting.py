"""
Change the Data Structure - Group Sorting

Algorithm: Page 432

Time complexity: O(n)
Auxiliary space: O(n)
"""

def group_array(array):
    hashTable = {}
    newArray = []
    
    for value in array:
        if hashTable.get(value) is not None:
            hashTable[value] += 1
        else:
            hashTable[value] = 1
            
    print(hashTable)
            
    for key, count in hashTable.items():
        for _ in range(count):
            newArray.append(key)
        
    return newArray
                
    


if __name__ == '__main__':
    arr = ["a", "c", "d", "b", "b", "c", "a", "d", "c", "b", "a", "d"]
    
    print(group_array(arr))