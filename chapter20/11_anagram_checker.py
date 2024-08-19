"""
Change the Data Structure - Anagram Checker

Algorithm: Page 428

Time complexity: O(n * m)
Auxiliary space: O(1)
"""

def anagramChecker(firstString, secondString):
    secondStringArray = list(secondString)
    
    for i in range(len(firstString)):
        if len(secondStringArray) == 0:
            return False
        
        for j in range(len(secondStringArray)):
            if firstString[i] == secondStringArray[j]:
                del secondStringArray[j]
                break
            
    return len(secondStringArray) == 0
    
    


if __name__ == '__main__':
    s1 = 'rattles'
    s2 = 'startle'
    s3 = 'scarlet'
    
    print(anagramChecker(s1, s2))
    print(anagramChecker(s1, s3))