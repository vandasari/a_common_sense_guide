"""
Greedy Algorithms - Array Max

Algorithm: Page 415

Time complexity: O(n)
"""

def findmax(array):
    # Greedily assume that the first number of the array is the greatest number:
    greatest_number = array[0]
    
    for num in array:
        if num > greatest_number:
            greatest_number = num
            
    return greatest_number