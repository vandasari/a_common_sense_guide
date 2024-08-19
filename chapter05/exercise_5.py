"""
Exercise 5

Time complexity: O(n^2) with n^2/2 steps
"""


def every_other(array):
    for index, number in enumerate(array):
        if index % 2 == 0:
            for other_number in array:
                print(
                    f"other_number = {other_number}; value = {array[index]}: {number} + {other_number} = {number + other_number}"
                )

            print("\n")


if __name__ == "__main__":
    arr = [4, 2, 7, 1, 3]

    every_other(arr)


"""
Returns:
    

"""
