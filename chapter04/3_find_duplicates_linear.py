""" 
A Linear Solution

Algorithm: page 58
Time complexity: O(n) or linear time.
Here the hasDuplicateValue() function takes n steps and combine with the find_max()
function which also takes n steps, in total there are 2n steps.
In terms of time complexity, the constant 2 is drop and hence O(n).

This new algorithm appears to make n comparisons for n data elements. This is because 
there’s only one loop, and it simply iterates for as many numbers as there are in the array.
"""


def find_max(arr):

    num_max = arr[0]
    steps = 0

    for i in arr:
        steps += 1
        if i > num_max:
            num_max = i

    return num_max, steps


def hasDuplicateValue(arr):
    nm, steps = find_max(arr)
    print(f"Steps from getting a max value = {steps}")
    existingNumbers = [None] * (int(nm) + 1)

    for i in range(len(arr)):
        steps += 1
        if existingNumbers[arr[i]] == 1:
            return True, steps
        else:
            existingNumbers[arr[i]] = 1

    return False, steps


if __name__ == "__main__":
    # myarr = [1, 5, 3, 9, 4, 1, 2]
    # myarr = [3, 5, 8]
    myarr = [1, 4, 5, 2, 9]
    # myarr = [5, 3, 8, 1, 2, 7]

    res, m = hasDuplicateValue(myarr)
    print(f"Has duplicates = {res}; total steps = {m}")


"""
Returns:
    
Steps from getting a max value = 5
Has duplicates = False; total steps = 10
"""
