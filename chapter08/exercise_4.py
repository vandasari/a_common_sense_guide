"""
Exercise 4 - Find The First Non-Duplicated Characters
Time complexity: O(n)

Write a function that returns the first non-duplicated character in a string. 
For example, the string, "minimum" has two characters that only exist once: 
the "n" and the "u", so your function should return the "n", since it occurs first. 
The function should have an efficiency of O(N).
"""


def findNonDuplicates(string):

    string = string.lower()

    hashTable = {}

    for i in string:
        if i not in hashTable.keys():
            hashTable[i] = 1
        else:
            hashTable[i] += 1

    # Iterate over the hash table
    # for j, k in hashTable.items():
    #     if k == 1:
    #         return j

    # Or, alternatively, iterate over the string again
    for j in string:
        if hashTable.get(j) == 1:
            return j


if __name__ == "__main__":
    # toSearch = 'minimum'
    toSearch = "oblivion"

    res = findNonDuplicates(toSearch)

    print(res)
