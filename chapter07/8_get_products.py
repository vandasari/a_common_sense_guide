"""
Algorithm; page 104
Time complexity: O(n^2) with n^2/2 steps
"""


def twoNumberProducts(array):
    products = []
    steps = 0

    # Outer array
    for i in range(len(array) - 1):
        # Inner array, in which j always begins one index to the right of i
        for j in range(i + 1, len(array)):
            steps += 1
            products.append(array[i] * array[j])

    return products, steps


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]

    res, m = twoNumberProducts(a)

    print(res)
    print(f"n = {len(a)}; steps = {m}")


"""
Returns:
    
[2, 3, 4, 5, 6, 8, 10, 12, 15, 20]
n = 5; steps = 10
"""
