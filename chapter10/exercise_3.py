"""
Exercise 3, page 160

Following is a function in which we pass in two numbers called low and high. 
The function returns the sum of all the numbers from low to high. For example, 
if low is 1, and high is 10, the function will return the sum of all numbers 
from 1 to 10, which is 55. However, our code is missing the base case, and will 
run indefinitely! Fix the code by adding the correct base case:
"""

def sum_all_numbers(low, high):    
    if low == high: # base case
        return low
    else:
        return high + sum_all_numbers(low, high - 1)
    
    
if __name__ == '__main__':
    res = sum_all_numbers(1, 10)
    print(res)