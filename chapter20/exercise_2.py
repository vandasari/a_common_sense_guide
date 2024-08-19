"""
Exercise 2 - Recognizing Patterns

Time complexity: O(n)
"""


def findMissingValue(array):
    full_sum = 0

    for n in range(len(array) + 1):
        full_sum += n

    current_sum = 0

    for num in arr:
        current_sum += num

    return full_sum - current_sum


if __name__ == "__main__":

    # arr = [2, 3, 0, 6, 1, 5]
    arr = [8, 2, 3, 9, 4, 7, 5, 0, 6]
    # arr = [0, 1, 3, 4, 5, 6]

    print(findMissingValue(arr))
