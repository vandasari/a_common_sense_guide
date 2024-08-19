"""
Insertion Sort

Algorithm: pages 84-85
Time complexity: O(n^2) with n^2 + 2n - 2 steps

Four types of steps occur in Insertion Sort: removals, comparisons, shifts, and insertions.

The insertion sort algorithm results in the different number of steps for each of
worst-case scenario, average-case scenario, and best-case scenario, as can 
be seen in the examples below.
For array with 10 elements (n = 10): 
    - worst-case scenario was executed with 45 comparisons & 45 shifts
    - average-case scenario was executed with 23 comparisons & 23 shifts 
    - best-case scenario was executed with 9 comparisons & 0 shifts
    
We can see that the performance of Insertion Sort varies greatly based on the scenario: 
    - In the worst-case scenario, Insertion Sort takes n^2 steps. 
    - In an average scenario, it takes n^2 / 2 steps. 
    - And in the best-case scenario, it takes about n steps.

"""

import random


def insertion_sort(array, sord):
    comp_steps = 0
    shift_steps = 0

    for index in range(1, len(array)):
        temp_value = array[index]

        # to the left of the temp_value; this keeps the position moving leftward:
        position = index - 1

        while position >= 0:
            comp_steps += 1
            if sord == "ascending":
                sorting_direction = array[position] > temp_value
            elif sord == "descending":
                sorting_direction = array[position] < temp_value

            # check if all values at position to the left of temp_value is greater than the temp_value
            if sorting_direction:
                # if it is, shift that value to the right:
                array[position + 1] = array[position]
                position -= 1
                shift_steps += 1

            else:
                break

        array[position + 1] = temp_value

    return array, comp_steps, shift_steps


if __name__ == "__main__":
    arr = [4, 2, 7, 1, 3]  # average-case scenario
    # arr = [5, 4, 3, 2, 1] # worst-case scenario of ascending; best-case scenario for descending
    # arr = [1, 2, 3, 4, 5] # best-case scenario for ascending; worst-case scenario for descending
    print(arr)

    res, mc, ms = insertion_sort(arr, "ascending")
    print(res)
    print(f"comparisons = {mc}; shifts = {ms}; total = {mc+ms} steps")

    print()

    # random.seed(10)
    myRandomArr = random.sample(range(1, 50), 10)  # average-case scenario
    # myRandomArr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # worst-case sceanario for ascending (completely reverse array)
    # myRandomArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # best-case scenario for ascending (already sorted array)

    print(myRandomArr)

    sorting_order = "ascending"

    # print(sorting_order)

    mySortedArr, nc, ns = insertion_sort(myRandomArr, sorting_order)
    print(mySortedArr)
    print(f"comparisons = {nc}; shifts = {ns}; total = {nc+ns} steps")
