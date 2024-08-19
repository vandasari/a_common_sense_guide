"""
Algorithm: page 96
Time complexity: O(n)

Time complexity:
    - worst-case scenario: since it takes 3n+3 steps, so O(n)
"""

import random


def average_of_even_numbers(array):
    _sum = 0.0 # 1 step
    count_event_numbers = 0 # 1 step
    
    for number in array: # 
        if number % 2 == 0: # n steps 
            _sum += number # n steps
            count_event_numbers += 1 # n steps
            
    return _sum / count_event_numbers # 1 step



if __name__ == '__main__':
    # random.seed(10)
        
    # a = [4, 2, 7, 1, 3]
    # b, n = selection_sort(a)
    # print(f'{b}, steps: {n}')
    
    myRandomArr = random.sample(range(1, 20), 10)
    
    print(myRandomArr)
    
    res = average_of_even_numbers(myRandomArr)
    
    print(f'Average of even numbers: {res}')