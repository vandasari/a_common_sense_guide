"""
Exercise 2
"""

def reverse(array):
    newArray = []
    
    for i in range(len(array)-1, -1, -1):
        newArray.append(array[i])
                    
    return newArray
        
   
if __name__ == '__main__':
    arr = [7, 1, 5, 2, 3, 4, 6, 9, 1]
    
    # Print original array
    print(arr) 
    
    # The resulted array after reversion, whose size is the same as the variable arr
    print(reverse(arr)) 
    
    # If we print again the variable of the original array variable and the array 
    # remains the same as the 1st print, it means auxiliary space O(n)
    print(arr) 


"""
Time complexity: O(n)
Auxiliary space: O(n)

Returns:
    
[7, 1, 5, 2, 3, 4, 6, 9, 1]
[1, 9, 6, 4, 3, 2, 5, 1, 7]
[7, 1, 5, 2, 3, 4, 6, 9, 1]
"""
