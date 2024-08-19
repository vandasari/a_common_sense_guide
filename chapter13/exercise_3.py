"""
Chapter: 13 Recursive Algorithms for Speed
Exercise: 3
Page: 224

Write three different implementations of a function that finds the greatest 
number within an array. Write one function that is O(N^2), one that is 
O(N log N), and one that is O(N). 
"""

import timeit


# Time complexity: O(n^2)
def findMax_v1(array):
    for i in range(len(array)):
        num_max = True
        for j in range(len(array)):
            if array[j] > array[i]:
                num_max = False
            
        if num_max:
            return array[i]

    
# Time complexity: O(n log(n))
def findMax_v2(array):
    array = sorted(array)
    return array[-1]


# Time complexity: O(n)
def findMax_v3(array):
    # num_max = float('-inf') # or 
    num_max = array[0]

    for i in array:
        if i > num_max:
            num_max = i
            
    return num_max


if __name__ == '__main__':
    arr = [5, 9, 3, 2, 4, 5, 6] 
    
    print('Version O(n^2):', timeit.timeit('[func(arr) for func in (findMax_v1, )]', globals=globals(), number=1), 'seconds')
    
    print('Version O(n log (n)):', timeit.timeit('[func(arr) for func in (findMax_v2, )]', globals=globals(), number=1), 'seconds')
    
    print('Version O(n):', timeit.timeit('[func(arr) for func in (findMax_v3, )]', globals=globals(), number=1), 'seconds')


