"""
Exercise 1

Use recursion to write a function that accepts an array of strings and returns 
the total number of characters across all the strings. For example, if the input 
array is ["ab", "c", "def", "ghij"], the output should be 10 since there are 10 
characters in total.
"""


def count_characters_loop(array):
    count = 0
    
    for string in array:
        count += len(string)
        
    return count


def count_characters_recursive(array):
    if len(array) == 1:
        return len(array[0])
    
    return len(array[0]) + count_characters_recursive(array[1:])



if __name__ == '__main__':
    arr = ['abc', 'd', 'ef']
    # arr = ["ab", "c", "def", "ghij"]
    
    print(count_characters_recursive(arr))

