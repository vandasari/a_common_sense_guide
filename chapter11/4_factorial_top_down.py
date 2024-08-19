"""
Calculate Factorial using Recursion with Top-Down Approach

factorial(5)
subproblem --> factorial(4) * factorial(3) * factorial(2) * factorial(1)
"""


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1) 
    
    
if __name__ == '__main__':
    num = 5
    res = factorial(num)
    print(f'{num}! = {res}')
    
 