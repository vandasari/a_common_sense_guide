""" 
Selection Sort

Algorithm: page 69
Time complexity: O(n^2) with n^2 / 2 steps

The selection sort algorithm is twice as fast as the bubble sort.

Both bubble sort and selection sort algorithms result in the same number of
COMPARISON steps for either worst-case scenario, average-case scenario, or 
best-case scenario, that is (n-1) + (n-2) + ... + 2 + 1, e.g.:

    n = 5   --> comparison = 4 + 3 + 2 + 1 = 10 steps
    n = 10  --> comparison = 9 + 8 + ... + 2 + 1 = 45 steps

However, the number of SWAP steps are different for each sorting algorithm:
- selection sort: we only need to make a maximum of one swap per pass-through
- bubble sort: we make a swap for each and every comparison within a pass-through

Maximum number of swaps (in worst-case scenario) for selection sort is (n - 1):

    n = 5   --> max swaps = 4 steps 
    n = 10  --> max swaps = 9 steps
    n = 20  --> max swaps = 19 steps
"""

import random


def selection_sort(array, sorting_order):
    comp_steps = 0
    swap_steps = 0

    for index in range(len(array) - 1):
        idx_lowest = index

        for j in range(index + 1, len(array)):
            if sorting_order == "ascending":
                comp_steps += 1
                if array[j] < array[idx_lowest]:  # comparison step
                    idx_lowest = j
            elif sorting_order == "descending":
                comp_steps += 1
                if array[j] > array[idx_lowest]:  # comparison step
                    idx_lowest = j

        if index != idx_lowest:  # swap step
            swap_steps += 1
            # temp = array[index]
            # array[index] = array[idx_lowest]
            # array[idx_lowest] = temp
            # -- or --
            array[index], array[idx_lowest] = array[idx_lowest], array[index]

    return array, comp_steps, swap_steps


if __name__ == "__main__":
    arr = [4, 2, 7, 1, 3]  # average-case scenario
    # arr = [5, 4, 3, 2, 1] # worst-case scenario for ascending; best-case scenario for descending
    # arr = [1, 2, 3, 4, 5] # best-case scenario for ascending; worst-case scenario for descending

    print(arr)

    res, nc, ns = selection_sort(arr, "ascending")
    print(res)
    print(f"n = {len(arr)}; comparisons = {nc}; swaps = {ns}; total = {nc+ns} steps")

    print()

    random.seed(10)

    # random array: average-case scenario
    # myArr = random.sample(range(1, 50), 10)

    # sorted array: best-case scenario for descending, worst-case scebario for ascending:
    # myArr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # sorted array: best-case scenario for ascending, worst-case scebario for descending:
    myArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(myArr)

    mySortedArr, mc, ms = selection_sort(myArr, "ascending")
    print(mySortedArr)
    print(f"n = {len(myArr)}; comparisons = {mc}; swaps = {ms}; total = {mc+ms} steps")

# ------------------------

"""
Returns:
    
[4, 2, 7, 1, 3]
[1, 2, 3, 4, 7]
n = 5; comparisons = 10; swaps = 2; total = 12 steps

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10; comparisons = 45; swaps = 0; total = 45 steps
"""
