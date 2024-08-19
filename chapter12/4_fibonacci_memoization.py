"""
Dynamic Programming through Memoization - Calculate Fibonacci Numbers

Algorithm: Pages 192--193
Time complexity: O(n)
"""


def fib(n, memo={}):
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Check the hash table (called memo) to see whether fib(n) was already
    # computed or not:
    if n not in memo.keys():
        # If n is NOT in memo, compute fib(n) with recursion and then store
        # the result in the hash table:
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)

    return memo[n]


# For displaying step-by-step execution:
def fib_steps(n, memo={}):
    print(f"recursion; push n = {n}")

    if n == 0:
        memo[n] = 0
        print(f"base case; memo = {memo}; return n = {n}")
        return 0
    if n == 1:
        memo[n] = 1
        print(f"base case; memo = {memo}; return n = {n}")
        return 1

    if n not in memo.keys():
        print(f"memo = {memo}; {n} not in memo")
        memo[n] = fib_steps(n - 2, memo) + fib_steps(n - 1, memo)
        print(f"n = {n}; memo = {memo}")

    return memo[n]


if __name__ == "__main__":
    # res = []
    # for i in range(12):
    #     res.append(fib(i))

    # print(res)

    num = 6
    res = fib_steps(num)
    print(res)

"""
Returns:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]    

Essentially, memoization reduces recursive calls by remembering previously computed 
functions.
"""
