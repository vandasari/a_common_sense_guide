"""
Exercise 1 - Intersection of Two Arrays
Time complexity: O(n)

Write a function that returns the intersection of two arrays. The intersection is 
a third array that contains all values contained within the first two arrays. 
For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4]. 
Your function should have a complexity of O(N). (If your programming language 
has a built-in way of doing this, don’t use it. The idea is to build the algorithm yourself.)
"""


def intersection(array1, array2):
    
    firstArray = {item: True for item in array1}
    
    intersect = []
    
    for i in array2:
        if firstArray.get(i) == True: # Check the value of the hash table 
            intersect.append(i)
            
    return intersect


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [0, 2, 4, 6, 8, 5]
    
    res = intersection(arr1, arr2)
    
    print(res)

"""
Returns:

[2, 4]
"""
    