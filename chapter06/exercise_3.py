"""
Exercise 3
Time complexity: O(n) for average-case scenario
                 O(n^2) for worst-case scenario
"""

import random


def twoSum(array):
    steps = 0
    for i in range(len(array)):
        for j in range(len(array)):
            steps += 1
            if i != j and array[i] + array[j] == 10:
                # steps += 1
                return True, steps
    return False, steps


if __name__ == "__main__":
    random.seed(11)

    myRandomArr = random.sample(range(1, 12), 10)  # average-case scenario
    print(myRandomArr)

    res1, m1 = twoSum(myRandomArr)
    print(res1, m1)

    print()

    worst = [29, 36, 30, 49, 33, 38, 13, 12, 45, 31]
    print(worst)

    res2, m2 = twoSum(worst)
    print(res2, m2)

    print()

    best = [1, 9, 2, 8, 3, 7, 4, 6, 0, 10]
    print(best)

    res3, m3 = twoSum(best)
    print(res3, m3)
