"""
Algorithm: page 103
Time complexity: O(n)

The while loop only runs until it reaches the midpoint of the string/word.
That would mean that the loop runs n/2 steps. However, time complexity is O(n).
"""


def isPalindrome(word):
    # Start the leftIndex at index 0
    leftIndex = 0
    # Start the rightIndex at the last index of array
    rightIndex = len(word) - 1
    
    halfArray = len(word) // 2
    
    while leftIndex < halfArray:
        if word[leftIndex] != word[rightIndex]:
            return False
        
        leftIndex += 1
        rightIndex -= 1
        
    return True


if __name__ == '__main__':
    words = ['racecar', 'kayak', 'tweet', 'deified']
    
    for a in words:
        res = isPalindrome(a)
        print(f'{a} is palindrome' if res==True else f'{a} is not palindrom')


