"""
Algorithm: page 102
Time complexity: O(n)

- The outer loop is iterating over the inner arrays, 
- The inner loop is iterating over the actual numbers. 
The inner loop only runs for as many numbers as there are in total.
This algorithm simply processes each number, hence the function’s time complexity is O(N).
"""

def count_ones(outer_array):
    count = 0
    
    for inner_array in outer_array: # the outer loop iterates over the inner array
        for number in inner_array: # the inner loop iterates over the actual array
            if number == 1:
                count += 1
                
    return count


if __name__ == '__main__':
    arr = [[0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0]]
    
    res = count_ones(arr)
    
    print(res)