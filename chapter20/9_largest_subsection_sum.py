"""
Greedy Algorithms - Largest Subsection Sum

Algorithm: Page 421

Time complexity: O(n)
Auxiliary space: O(1)
"""

def largestSum(array):
    current_sum = 0
    greatest_sum = 0
    
    for num in array:
        # If current sum is a negative number, reset current sum to zero:
        if current_sum + num < 0:
            current_sum = 0
        else:
            current_sum += num
            
            # Greedily assume the current sum is the greatest sum if it's the
            # greatest sum we've encountered so far:
            if current_sum > greatest_sum:
                greatest_sum = current_sum 
                
    return greatest_sum


if __name__ == '__main__':
    arr = [3, -4, 4, -3, 5, -9]
    
    print(largestSum(arr))