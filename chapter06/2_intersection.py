"""
A Practical Example

Algorithm: page 91
Time complexity: O(n^2) or O(nxm) if arrays have different sizes
    
The intersection is a list of all the values that occur in both of the arrays. 
For example, if you have the arrays, [3, 1, 4, 2] and [4, 5, 3, 6], the intersection 
would be a third array, [3, 4], since both of those values are common to the two arrays.
"""

import random


def intersection_v1(array1, array2):
    """
    Time complexity: O(n^2) or O(nxm) if arrays have different sizes for all 3 scenarios
    """

    result = []
    steps = 0
    
    for i in range(len(array1)):
        for j in range(len(array2)):
            steps += 1
            if array1[i] == array2[j]:
                result.append(array1[i])
                
    return result, steps


def intersection_v2(array1, array2):
    """
    Time complexity:
        - worst-case scenario: O(n^2)
        - best-case scenario: O(n) --> when the two arrays are identical
        - average-case scenario: between O(n) and O(n^2)
    """

    result = []
    steps = 0
    
    for i in range(len(array1)):
        for j in range(len(array2)):
            steps += 1
            if array1[i] == array2[j]:              
                result.append(array1[i])
                break
                
    return result, steps



if __name__ == '__main__':
    random.seed(11)
    
    myRandomArr1 = random.sample(range(1, 50), 10) 
    myRandomArr2 = random.sample(range(1, 50), 10) 
    
    # print(myRandomArr1)
    # print(myRandomArr2)
    
    res1, m1 = intersection_v1(myRandomArr1, myRandomArr2)
    res2, m2 = intersection_v2(myRandomArr1, myRandomArr2)
    print(f'version 1: {res1}; steps: {m1}')
    print(f'version 2: {res2}; steps: {m2}')
    
    print()
    
    # Try out with identical arrays
    arr1 = [3, 1, 4, 2, 6, 9, 7, 8, 0, 10]
    arr2 = [3, 1, 4, 2, 6, 9, 7, 8, 0, 10]
    
    result1, n1 = intersection_v1(arr1, arr2)
    result2, n2 = intersection_v2(arr1, arr2)
    print(f'version 1: {result1}; steps: {n1}')
    print(f'version 2: {result2}; steps: {n2}')