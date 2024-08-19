"""
Calculate Triangle Numbers with Top-Down Approach

Algorithm: page 170
"""

import random


def sum_array(array):
    # base caseL only one element in the array
    if len(array) == 1:
        return array[0]
    return array[0] + sum_array(array[1:len(array)]) 


if __name__ == '__main__':    
    # myArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    myArr = random.sample(range(1, 10), 5)
        
    print(myArr)
    
    res = sum_array(myArr)
    
    print(f'Sum of the array = {res}')

