"""
Exercise 5

Unique Paths
"""


def unique_paths(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    return unique_paths(rows - 1, cols) + unique_paths(rows, cols - 1)
    


if __name__ == '__main__':    
    r = 3
    c = 7
    res = unique_paths(r, c)
    print(res)

     


"""

"""