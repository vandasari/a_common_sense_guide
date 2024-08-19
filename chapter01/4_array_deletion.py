"""
Array Deletion

Time complexity: O(1) for deletion at the end of array
                 O(n) for deletion at the beginning of array
"""


# Time complexity: O(1)
def delete_at_end(array):
    newarray = [0] * (len(array) - 1)
    newarray = array[:-1]
    return newarray


# Time complexity: O(n)
def delete_at_beginning(array):
    newarray = [0] * (len(array) - 1)
    newarray = array[1:]
    return newarray


def delete_anywhere(array, pos):
    return array[:pos] + array[pos + 1 :]


if __name__ == "__main__":
    arr = ["apples", "bananas", "cucumbers", "dates", "elderberries"]

    print(delete_at_end(arr))

    # arr = ['apples', 'bananas', 'cucumbers', 'dates', 'elderberries']

    print(delete_at_beginning(arr))

    # arr = ['apples', 'bananas', 'cucumbers', 'dates', 'elderberries']

    print(delete_anywhere(arr, 2))  # delete 'cucumbers'
