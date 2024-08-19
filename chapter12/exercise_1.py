"""
Chapter: 12 Dynamic Programming
Exercise: 1 
Page: 197

The following function accepts an array of numbers and returns the sum, as long 
as a particular number doesn’t bring the sum above 100. If adding a particular 
number will make the sum higher than 100, that number is ignored. However, this 
function makes unnecessary recursive calls. Fix the code to eliminate the 
unnecessary recursion:
"""

def add_until_100_question(array):
    if len(array) == 0:
        return 0
    
    if array[0] + add_until_100_question(array[1:]) > 100:
        return add_until_100_question(array[1:])
    else:
        return array[0] + add_until_100_question(array[1:])
    

# Solution to reduces unnecessary recursive calls:
def add_until_100_solution(array):
    if len(array) == 0:
        return 0
    
    temp = add_until_100_solution(array[1:])
    
    if array[0] + temp > 100:
        return temp
    else:
        return array[0] + temp


if __name__ == '__main__':
    arr = [80, 2, 4, 9, 10]
    res = add_until_100_solution(arr)
    print(res)

"""
Returns:
25
"""