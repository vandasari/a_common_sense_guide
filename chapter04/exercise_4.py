"""
Exercise 4 on page 61
Change algorithm from O(n^2) to O(n).
"""


# Time complexity O(n^2)
def greatestNumberSlow(array):
    steps = 0
    for i in array:
        max_val = True

        for j in array:
            steps += 1
            if j > i:
                max_val = False

        if max_val:
            return i, steps


# Time complexity O(n)
def greatestNumberFast(array):
    val_max = array[0]
    steps = 0

    for i in array:
        steps += 1
        if i > val_max:
            val_max = i

    return val_max, steps


if __name__ == "__main__":
    myarr = [1, 4, 5, 2, 9]

    res1, m = greatestNumberSlow(myarr)
    res2, n = greatestNumberFast(myarr)

    print(f"Results slow algorithm: max number = {res1}, steps = {m}")
    print(f"Results fast algorithm: max number = {res2}, steps = {n}")
