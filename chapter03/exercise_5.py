"""
Exercise 5
Time complexity: O(1)
"""


def median(array):
    middle = len(array) // 2
    
    if len(array) % 2 == 0:
        return (array[middle - 1] + array[middle]) / 2.
    else:
        return array[middle]
    
    
if __name__ == '__main__':
    nums = [16, 32, 64, 128, 256, 512, 1024]
    
    res = median(nums)
    print(res)