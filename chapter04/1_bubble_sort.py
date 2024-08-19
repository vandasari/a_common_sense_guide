""" 
Sorting Algorithms - Bubble Sort

Algorithm: page 52
Time complexity: O(n^2) or quadratic time

n = 5   --> comparison = 10 steps;  swap = max 10 (for worst-case scenario);  total = 20 steps
n = 10  --> comparison = 45 steps;  swap = max 45 (for worst-case scenario);  total = 90 steps
"""

import random


def bubble_sort(array, sorting_order):
    unsorted_until_index = len(array) - 1 # keeps track of the rightmost index of array
    is_sorted = False
    comp_steps = 0
    swap_steps = 0
    
    while not is_sorted:
        
        for i in range(unsorted_until_index):
            if sorting_order == 'ascending':
                # Comparison:
                comp_steps += 1
                if array[i] > array[i+1]:
                    # Swap:
                    array[i], array[i+1] = array[i+1], array[i] # swap
                    swap_steps += 1
                    # print(f'swap {swap_steps}: {array}')
            elif sorting_order == 'descending':
                comp_steps += 1
                if array[i] < array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i]
                    swap_steps += 1
                    # print(f'swap {swap_steps}: {array}')
                
        unsorted_until_index -= 1
        
        if unsorted_until_index == 0:
            is_sorted = True
        
    return array, comp_steps, swap_steps
        
        

if __name__ == '__main__':        
    arr = [4, 2, 7, 1, 3] # average-case scenario
    # arr = [5, 4, 3, 2, 1] # worst-case scenario for ascending order; best-case scenario for descending order
    arr = [1, 2, 3, 4, 5] # worst-case scenario for descending order; best-case scenario for ascending order
    
    print(arr)
    
    res, mc, ms = bubble_sort(arr, 'descending')
    print(res)
    print(f'n = {len(arr)}; comparisons = {mc}; swaps = {ms}; total = {mc+ms} steps')
    
    print()
    #----------------------#
    
    random.seed(10)
    
    myRandomList = random.sample(range(1, 50), 10)
    
    print(myRandomList)
    
    mySortedList, nc, ns = bubble_sort(myRandomList, 'ascending')
        
    print(mySortedList)
    print(f'n = {len(myRandomList)}; comparisons = {nc}; swaps = {ns}; total = {nc+ns} steps')


"""
Returns:
    
[4, 2, 7, 1, 3]
[7, 4, 3, 2, 1]
n = 5; comparisons = 10; swaps = 4; total = 14 steps

[37, 3, 28, 31, 49, 1, 14, 30, 32, 18]
[1, 3, 14, 18, 28, 30, 31, 32, 37, 49]
n = 10; comparisons = 45; swaps = 23; total = 68 steps
"""