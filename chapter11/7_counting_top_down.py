"""
Counting X with Top-Down Approach

Algorithm: page 172-173
"""

def count_x(string):
    # base case: an empty string
    if len(string) == 0:
        return 0
    
    if string[0] == 'x':
        return 1 + count_x(string[1:len(string)])

    return count_x(string[1:len(string)]) 


if __name__ == '__main__': 
    word = 'axbxcxd'
    # word = 'abcdefg'
    # word = 'zyxuvwx' 
    
    res = count_x(word)
    print(f"There are {res} x's in {word}")


