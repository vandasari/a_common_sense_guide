"""
The Little Fix for Big O

Algorithm: page 187

Time complexity: O(n)
"""


def find_max(array):
    if len(array) == 1:  # base case
        return array[0]

    # Calculate the max of the remainder of the array and store it inside a variable:
    max_of_remainder = find_max(array[1:])

    # Comparison of first number against this variable:
    if array[0] > max_of_remainder:
        return array[0]
    else:
        return max_of_remainder


# For displaying step-by-step execution:
def find_max_steps(array):
    print(f"recursion; array = {array}; push {array[0]}")
    if len(array) == 1:  # base case
        print(f"base case: return {array[0]}")
        return array[0]

    max_of_remainder = find_max_steps(array[1:])
    print(f"max_of_remainder = {max_of_remainder}")

    if array[0] > max_of_remainder:
        print(
            f"pop {array[0]} where {array[0]} > {max_of_remainder}; return {array[0]}"
        )
        return array[0]
    else:
        print(
            f"pop {array[0]} where {array[0]} < {max_of_remainder}; return {max_of_remainder}"
        )
        return max_of_remainder


if __name__ == "__main__":
    arr = [1, 4, 11, 10, 6]
    res = find_max_steps(arr)
    print(res)
