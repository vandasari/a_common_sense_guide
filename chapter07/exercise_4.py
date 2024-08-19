"""
Exercise 4 - Find the Greatest Product of Three Numbers from an Array
Time complexity: O(n^3)
"""


def largest_product(array):
    largest_product_so_far = array[0] * array[1] * array[2]
    i = 0
    steps = 0
    
    while i < len(array):
        j = i + 1
        
        while j < len(array):
            k = j + 1
            
            while k < len(array):
                steps += 1
                if array[i] * array[j] * array[k] > largest_product_so_far:
                    largest_product_so_far = array[i] * array[j] * array[k]
                    
                k += 1
                
            j += 1
            
        i += 1
        
    return largest_product_so_far, steps


if __name__ == '__main__':    
    arr = [1, 3, 5, 6, 7, 9, 10, 20]
    
    res, m = largest_product(arr)
    print(f'largest product = {res}, steps = {m}')
    