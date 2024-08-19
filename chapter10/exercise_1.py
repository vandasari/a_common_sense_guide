"""
Exercise 1

The following function prints every other number from a low number to a high number. 
For example, if low is 0 and high is 10, it would print:
0 
2 
4 
6 
8 
10
"""

def print_every_other(low, high):
    if low > high: # base case
        return
    else:
        print(low)
        print_every_other(low + 2, high)


if __name__ == '__main__':
    print_every_other(0, 10)