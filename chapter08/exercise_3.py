"""
Exercise 3 - Find Missing Letters
Time complexity: O(n)

Write a function that accepts a string that contains all the letters of the alphabet 
except one and returns the missing letter. For example, the string, 
"the quick brown box jumps over a lazy dog" contains all the letters of the alphabet 
except the letter, "f". The function should have a time complexity of O(N).
"""


def findMissingLetters(string, letters):

    toSearch = {item: True for item in string}

    missing = []

    for i in letters:
        if i not in toSearch.keys():
            missing.append(i)

    return missing


if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    myString = "the quick brown box jumps over a lazy dog"

    res = findMissingLetters(myString, alphabet)

    print(res)

"""
Returns

['f']
"""
