"""
Chapter: 13 Recursive Algorithms for Speed
Exercise: 1
Page: 224

Given an array of positive numbers, write a function that returns the greatest 
product of any three numbers. The approach of using three nested loops would 
clock in at O(N3), which is very slow. Use sorting to implement the function in 
a way that it computes at O(N log N) speed. (There are even faster implementations, 
but we’re focusing on using sorting as a technique to make code faster.)

Solution:
"""

def greatestProductOf3(array):
    array = sorted(array) # time complexity: O(n log(n))
    
    # Return multiplication of the last 3 items:
    return array[len(array)-1] * array[len(array) - 2] * array[len(array) - 3]


if __name__ == '__main__':
    arr = [5, 9, 3, 2, 4, 5, 6]
    
    res = greatestProductOf3(arr)
    print(res)

