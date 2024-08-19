"""
Array Searching

Time complexity: O(n)
"""


def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i


if __name__ == '__main__':
    myarray = ['apples', 'bananas', 'cucumbers', 'dates', 'elderberries']
    
    print(linear_search(myarray, 'dates'))