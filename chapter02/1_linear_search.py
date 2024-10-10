"""
Ordered Arrays - Linear Search

Algorithm: page 25
Time complexity: O(n) 

The linear search algorithm can work ordered and unordered arrays.
"""


def linear_search_v1(arr, search_value):
    for i in range(len(arr)):
        if arr[i] == search_value:
            return i
        elif arr[i] > search_value:
            break

    return None


def linear_search(array, search_value):
    for index, element in enumerate(array):
        if element == search_value:
            return index
        elif element > search_value:
            break

    return None


if __name__ == "__main__":

    orderedArray = [3, 5, 9, 11, 17, 75, 80, 92, 101, 123, 156, 178, 202]
    # unorderedArray = [10, 3, 5, 19, 11, 17, 75, 80, 92, 101, 123, 156, 22, 178, 202]

    c = 11

    res = linear_search_v1(orderedArray, c)

    print(
        "Item not found"
        if res == None
        else f"{orderedArray[res]} is found at index {res}."
    )
