"""
Exercise 4

Use recursion to write a function that accepts a string and returns the first 
index that contains the character “x.” For example, the string, 
"abcdefghijklmnopqrstuvwxyz" has an “x” at index 23. To keep things simple, 
assume the string definitely has at least one “x.”
"""


def index_of_first_x(string):
    if 'x' not in string:
        return "The string does not contain an x"
    else:
        if string[0] == 'x':
            return 0
        return index_of_first_x(string[1:]) + 1
    


if __name__ == '__main__':
    s = 'abcdefghijklmnopqrstuvwxyz'
    
    print(index_of_first_x(s))

     


"""

"""