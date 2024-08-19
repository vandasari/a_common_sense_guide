"""
Exercise 2
Time complexity: O(n)
"""


def arraySum(array):
    _sum = 0
    
    for i in range(len(array)):
        _sum += array[i]
        
    return _sum
    
    
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(arraySum(arr))
