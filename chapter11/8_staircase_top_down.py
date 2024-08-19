"""
The Staircase Problem with Top-Down Approach

Algorithm: page 177
"""

def number_of_paths(n):
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
    else:
        return number_of_paths(n - 1) + number_of_paths(n - 2) + number_of_paths(n - 3)



if __name__ == '__main__':
    paths = 11
    res = number_of_paths(paths)
    print(res)


