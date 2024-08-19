"""
Algorithm on page 189

Overlapping Subproblems

Time complexity: O(2^n)
"""


def fib(n):
    if n == 0 or n == 1:  # base case
        return n
    return fib(n - 2) + fib(n - 1)


# For displaying step-by-step execution:
def fib_steps(n):
    print(f"recursion; push: n = {n}")
    if n == 0 or n == 1:  # base case
        print(f"base case: return n = {n}")
        return n
    return fib_steps(n - 2) + fib_steps(n - 1)


if __name__ == "__main__":
    # res = []
    # for i in range(12):
    #     res.append(fib(i))

    # print(res)

    num = 5
    res = fib_steps(num)


"""
The line "return fib(n - 2) + fib(n - 1)" shows us that the function calls itself 
twice and suffers from the time complexity O(2^n).

Returns:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]   
"""
