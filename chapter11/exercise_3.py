"""
Exercise 3

There is a numerical sequence known as “Triangular Numbers.” The pattern begins 
as 1, 3, 6, 10, 15, 21, and continues onward with the Nth number in the pattern, 
which is N plus the previous number. For example, the 7th number in the sequence 
is 28, since it’s 7 (which is N) plus 21 (the previous number in the sequence). 
Write a function that accepts a number for N and returns the correct number from 
the series. That is, if the function was passed the number 7, the function would 
return 28.
"""


def triangular_number(n):
    if n == 1:
        return 1
    return n + triangular_number(n - 1)


if __name__ == '__main__':
    num = 7
    
    print(triangular_number(num))


"""
n = 1   --> t(1) = 1
n = 2   --> t(2) = 2 + t(1) = 2 + 1 = 3
n = 3   --> t(3) = 3 + t(2) = 3 + 3 = 6
n = 4   --> t(4) = 4 + t(3) = 4 + 6 = 10
n = 5   --> t(5) = 5 + t(4) = 5 + 10 = 15
n = 6   --> t(6) = 6 + t(5) = 6 + 15 = 21
n = 7   --> 7 + 21 = 28
"""