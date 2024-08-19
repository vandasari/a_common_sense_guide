"""
Exercise 3
Time complexity: O(n^2)
"""


def greatestProduct(array):
    greatestProductSoFar = array[0] * array[1]
    steps = 0
    
    for i, iVal in enumerate(array):
        for j, jVal in enumerate(array):
            steps += 1
            if i != j and iVal * jVal > greatestProductSoFar:
                greatestProductSoFar = iVal * jVal
                
    return greatestProductSoFar, steps


if __name__ == '__main__':
    myarr = [1, 4, 5, 2, 9]
    
    res, s = greatestProduct(myarr)
    print(f'Greates product = {res}, steps = {s}')