"""
Unnecessary Recursive Calls

Algorithm: pages 183--184

Time complexity: O(2^n)
"""


def find_max(array):
    # print('recursion')
    if len(array) == 1:  # base case
        return array[0]

    if array[0] > find_max(array[1:]):
        return array[0]
    else:
        return find_max(array[1:])


# For displaying step-by-step execution:
def find_max_steps(array):
    print(f"recursion; array = {array}; push {array[0]}")

    if len(array) == 1:  # base case
        print(f"base case, return: {array[0]}")
        return array[0]

    if array[0] > find_max_steps(array[1:]):
        print(f"pop {array[0]} where {array[0]} > function; return {array[0]}")
        return array[0]
    else:
        print(f"Else: {array[0]} < function; call recursion")
        temp = find_max_steps(array[1:])
        print(f"pop: {array[0]}; array = {array}")
        print(f"return temp = {temp}")
        return temp


if __name__ == "__main__":
    arr = [1, 4, 10, 6]
    res = find_max_steps(arr)
    print(res)
