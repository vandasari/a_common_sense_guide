"""
Chapter: 12 Dynamic Programming
Exercise: 2 
Page: 197

The following function uses recursion to calculate the Nth number from a mathematical 
sequence known as the “Golomb sequence.” It’s terribly inefficient, though! 
Use memoization to optimize it. (You don’t have to actually understand how the 
Golomb sequence works to do this exercise.)
"""

def golomb_question(n):
    if n == 1:
        return 1
    
    return 1 + golomb_question(n - golomb_question(golomb_question(n - 1)))


# The solution is by using memoization for optimization:
def golomb_solution(n, memo={}):    
    if n == 1:
        return 1

    if n not in memo.keys(): 
        memo[n] = 1 + golomb_solution(n - golomb_solution(golomb_solution(n - 1, memo), memo), memo)
        
    return memo[n]


if __name__ == '__main__':
    num = 20
    res = []
    for i in range(1, num):
        res.append(golomb_solution(i))
        
    print(res)


"""
Returns:
    
[1, 2, 2, 3, 3,  4, 4, 4, 5, 5, 5,  6, 6, 6, 6, 7, 7, 7, 7]

n = 5   -> 3 calls
n = 10  -> 8 calls
n = 20  -> 18 calls
"""