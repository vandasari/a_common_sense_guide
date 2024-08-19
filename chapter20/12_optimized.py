"""
Change the Data Structure - Optimized Anagram Checker

Algorithm: Page 429--430

Time complexity: O(n + m)
Auxiliary space: O(n)
"""

def anagramChecker(firstString, secondString):
    firstWordHashTable = {}
    secondWordHashTable = {}
    
    for char in firstString:
        if firstWordHashTable.get(char) is not None:
            firstWordHashTable[char] += 1
        else:
            firstWordHashTable[char] = 1
            
    for char in secondString:
        if secondWordHashTable.get(char) is not None:
            secondWordHashTable[char] += 1
        else:
            secondWordHashTable[char] = 1
            
    return firstWordHashTable == secondWordHashTable
    
    


if __name__ == '__main__':
    s1 = 'rattles'
    s2 = 'startle'
    s3 = 'scarlet'
    
    print(anagramChecker(s1, s2))
    print(anagramChecker(s1, s3))