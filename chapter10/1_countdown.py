"""
Algorithm: page 151
"""


def countdown(number):
    print(number)
    # base case, to prevent the function calls itself indefinitely
    if number == 0:
        return
    else:
        return countdown(number - 1)


if __name__ == "__main__":
    countdown(4)
