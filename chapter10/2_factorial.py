"""
Algorithm: page 152
"""


def factorial(number):
    if number < 0:  # base case
        return
    elif number < 2:  # base case
        return 1
    else:
        return number * factorial(number - 1)


# For displaying step-by-step execution:
def factorial_steps(number):
    print(f"push: n = {number}")
    if number < 0:  # base case
        print(f"base case: {number} < 0 --> do nothing")
        return
    elif number < 2:  # base case
        print(f"base case: {number} < 2 --> return 1")
        return 1
    else:
        print(f"n > 2 => {number} > 2; call the function")
        temp = number * factorial_steps(number - 1)
        print(f"pop n = {number}; factorial({number - 1})")
        print(f"return temp = {temp}")
        return temp


if __name__ == "__main__":
    num = 5
    res = factorial_steps(num)
    print(f"{num}! = {res}")
