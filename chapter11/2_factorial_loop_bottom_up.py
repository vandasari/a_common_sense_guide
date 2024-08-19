"""
Calculate Factorial using Loop with Bottom-up Approach
Algorithm: page 166
"""

def factorial(n):
    product = 1
    
    for num in range(1, n+1):
        product *= num
    
    return product


if __name__ == '__main__':
    num = 5
    res = factorial(num)
    print(f'{num}! = {res}')

