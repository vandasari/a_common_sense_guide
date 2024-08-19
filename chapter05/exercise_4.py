"""
Exercise 4

Time complexity: O(n) with 3n steps
"""
    
def multiple_cases(array):
    for string in array:
        print(string.upper())
        print(string.lower())
        print(string.capitalize())
        
        
if __name__ == '__main__':
    arr = ['apple', 'banana', 'cranberry', 'drone']
    
    multiple_cases(arr)
    
    
"""
Returns:
    
APPLE
apple
Apple
BANANA
banana
Banana
CRANBERRY
cranberry
Cranberry
DRONE
drone
Drone
"""