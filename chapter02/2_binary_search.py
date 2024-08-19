"""
Ordered Arrays - Binary Search

Algorithm: page 29--30
Time complexity: O(log(n)) 

The binary search algorithm only works with ordered/sorted arrays.
"""


def binary_search(array, search_value):
    lower_bound = 0  # index at the lowest
    upper_bound = len(array) - 1  # index at the highest

    while lower_bound <= upper_bound:
        # Within the loop, our code inspects the value at the midpoint of the range.
        midpoint = (lower_bound + upper_bound) // 2

        # We inspect the value at the midpoint:
        guess = array[midpoint]

        if guess == search_value:
            return guess, midpoint
        elif guess > search_value:
            upper_bound = midpoint - 1
        elif guess < search_value:
            lower_bound = midpoint + 1
        else:
            break

    return None, None


if __name__ == "__main__":
    orderedArray = [3, 5, 9, 11, 17, 75, 80, 92, 101, 123, 156, 178, 202]
    # unorderedArray = [10, 3, 5, 19, 11, 17, 75, 80, 92, 101, 123, 156, 22, 178, 202]

    c = 11

    res, idx = binary_search(orderedArray, c)

    print("Item not found" if res == None else f"{res} is found at index {idx}.")
