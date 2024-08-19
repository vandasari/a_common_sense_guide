"""
Algorithm: page 99
Time complexity: O(1) with 3 steps --> remember, reading of arrays is alaways O(1)
"""

import random


def sample(array):
    
    first = array[0]
    middle = array[int( len(array)/ 2)]
    last = array[-1]
    
    return [first, middle, last]


if __name__ == '__main__':    
    myRandomArr = random.sample(range(1, 20), 10)
    
    print(myRandomArr)
    
    r1, r2, r3 = sample(myRandomArr)
    
    print(f'First: {r1}, middle: {r2}, last: {r3}')