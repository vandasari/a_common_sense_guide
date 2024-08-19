"""
Array Insertion

Time complexity: O(1) for insertion at the end of array
                 O(n) for insertion at the beginning of array
"""


# Time complexity: O(1)
def insert_at_end(array, value):
    array.append(value)
    return array


# This function and others below are inefficient and will be clearly understood
# after learning Chapter 19:
def inefficient_insert_at_end(array, value):
    return array + [value]


# Time complexity: O(n)
def insert_at_beginning(array, value):
    return [value] + array


def insert_anywhere(array, value, pos):
    return array[:pos] + [value] + array[pos:]


if __name__ == "__main__":
    arr = ["apples", "bananas", "cucumbers", "dates", "elderberries"]

    print(insert_at_end(arr, "mangos"))

    print(insert_at_beginning(arr, "mangos"))

    # print(insert_anywhere(arr, 'mangos', 3))
