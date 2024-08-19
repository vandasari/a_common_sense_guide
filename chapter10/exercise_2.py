"""
Exercise 2

My kid was playing with my computer and changed my factorial function so that 
it computes factorial based on (n - 2) instead of (n - 1). Predict what will 
happen when we run factorial(10) using this function:
"""


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 2)


if __name__ == "__main__":
    num = 10
    res = factorial(num)
    print(f"{num}! = {res}")


"""
factorial(10) = 10 * 8 * 6 * 4 * 2 = 3840
factorial(5) = 5 * 3 * 1 = 15
"""
