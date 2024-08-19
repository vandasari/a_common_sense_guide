"""
Exercise 3

Create a new function to reverse an array that takes up just O(1) extra space.
"""

def reverse(array):
    n = len(arr)
    
    for i in range(len(array)):
        if i < len(array) // 2:
            array[i], array[n-i-1] = array[n-i-1], array[i]
            
    return array
        
   
if __name__ == '__main__':
    arr = [7, 1, 5, 2, 3, 4, 6, 9, 1]
    
    # Print original array
    print(arr) 
    
    # The resulted array after reversion, whose size is the same as the variable arr
    print(reverse(arr)) 
    
    # If we print again the original array variable and now the array has changed 
    # following the resulted array after reversion, it means auxiliary space O(1)
    print(arr) 


"""
Time complexity: O(n)
Auxiliary space: O(1)

Returns:
    
[7, 1, 5, 2, 3, 4, 6, 9, 1]
[1, 9, 6, 4, 3, 2, 5, 1, 7]
[1, 9, 6, 4, 3, 2, 5, 1, 7]
"""
