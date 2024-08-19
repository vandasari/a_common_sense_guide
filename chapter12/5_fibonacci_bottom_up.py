"""
Dynamic Programming through Going Bottom-Up - Calculate Fibonacci Numbers

Algorithm: Page 195
Time complexity: O(n)
"""

def fib(n):
    if n == 0:
        return 0
    
    a, b = 0, 1
    
    for i in range(1, n):
        # temp = a
        # a = b
        # b = temp + a
        # or
        a, b = b, a + b
        
    return b
    

if __name__ == '__main__':
    res = []
    for i in range(12):
        res.append(fib(i))
    
    print(res)

"""
Returns:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]    


Generally speaking, going bottom-up is often the better choice unless the 
recursive solution is more intuitive, in which case, you can keep the recursion
and keep it fast using memoization.
"""