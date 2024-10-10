""" 
A Quadratic Problem

Algorithm: page 57
Time complexity: O(n^2) or quadratic time

Very often (but not always), when an algorithm nests one loop inside another, 
the algorithm is O(n^2).
"""


def hasDuplicateValue(array):
    steps = 0
    for i in range(len(array)):
        for j in range(len(array)):
            steps += 1
            # Comparison:
            if i != j and array[i] == array[j]:
                return True, steps
    return False, steps


if __name__ == "__main__":
    # myarr = [1, 5, 3, 9, 4]
    myarr = [1, 4, 5, 2, 9]

    res, n = hasDuplicateValue(myarr)

    print(f"Has duplicates = {res}; steps taken = {n}")


"""
Returns:
    
Has duplicates = False; steps taken = 25
"""
