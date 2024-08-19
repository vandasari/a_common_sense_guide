"""
Algorithm: page 105
Time complexity: O(n*m)
where n is the size of array1 and m is the size of array2.

O(n*m) can be construed as a range between O(n) and O(n^2)
"""


def twoNumberProducts(array1, array2):
    products = []
    steps = 0
    
    for i in range(len(array1)):
        for j in range(len(array2)):
            steps += 1
            products.append(array1[i] * array2[j])
            
    return products, steps


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [10, 20, 40, 80]
    
    res, m = twoNumberProducts(a, b)
    
    print(res)
    print(f'n1 = {len(a)}, n2 = {len(b)}, steps = {m}')

"""
Returns:
    
[10, 20, 40, 80, 20, 40, 80, 160, 30, 60, 120, 240]
n1 = 3, n2 = 4, steps = 12
"""