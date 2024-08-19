"""
Exercise 2

Use recursion to write a function that accepts an array of numbers and returns 
a new array containing just the even numbers.
"""


def array_of_even_numbers(array):
    new_array = []
    
    for num in array:
        if num % 2 == 0:
            new_array.append(num)
            
    return new_array


def array_of_even_numbers_recursive(array):
    
    if len(array) == 0:
        return []
    
    if array[0] % 2 == 0:
        return [array[0]] + array_of_even_numbers_recursive(array[1:])
    else:
        return array_of_even_numbers_recursive(array[1:])
    


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(array_of_even_numbers_recursive(arr))

