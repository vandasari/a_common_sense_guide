"""
Exercise 1
Time complexity: O(1)
"""


def isLeapYear(year):
    if year % 100 == 0 or year % 400 == 0 or year % 4 == 0:
        return True
    else:
        return False
    
    
if __name__ == '__main__':
    print(isLeapYear(2024))
