"""
Exercise 4
Time complexity: O(n)
"""


def selectAString(array):
    newArray = []
    
    for i in range(len(array)):
        if array[i].startswith('a'):
            newArray.append(array[i])
            
    return newArray
    
    
if __name__ == '__main__':
    names = ['apples', 'books', 'candies', 'air conditioner']
    
    res = selectAString(names)
    print(res)