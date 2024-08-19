"""
Exercise 1
Time complexity: O(n)
"""

def one_hundred_sum(array):
    left_index = 0
    right_index = len(array) - 1
    steps = 0
    
    while left_index < len(array) // 2:
        steps += 1
        if array[left_index] + array[right_index] != 100:
            return False, steps
        
        left_index += 1
        right_index -= 1
        
    return True, steps


if __name__ == '__main__':
    # import random
    
    # arr = random.sample(range(1, 50), 10)
    
    arr = [20, 10, 40, 70, 50, 50,30, 60, 90, 80]
    
    print(arr)
    
    res, m = one_hundred_sum(arr)
    print(res)
    print(f'steps = {m}')