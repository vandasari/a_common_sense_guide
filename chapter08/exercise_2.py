"""
Exercise 2
Time complexity: O(n)

Write a function that accepts an array of strings and returns the first duplicate 
value it finds. For example, if the array is ["a", "b", "c", "d", "c", "e", "f"], 
the function should return "c", since it’s duplicated within the array. 
(You can assume that there’s one pair of duplicates within the array.) Make sure 
the function has an efficiency of O(N).
"""


def findDuplicates(toSearch):

    hashTable = {}

    duplicates = []

    for i in toSearch:
        if i in hashTable.keys():
            duplicates.append(i)
        else:
            hashTable[i] = True

    return duplicates


if __name__ == "__main__":
    arr = ["a", "b", "c", "d", "c", "e", "f"]

    res = findDuplicates(arr)

    print(res)

# ------

"""
Returns

['c']
"""
