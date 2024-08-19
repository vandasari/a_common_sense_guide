"""
Chapter: 12 Dynamic Programming
Exercise: 3 
Page: 197

Here is a solution to the “Unique Paths” problem from an exercise in the previous 
chapter. Use memoization to improve its efficiency.

Solution:
"""

def unique_paths(rows, cols, memo={}):
    if rows == 1 or cols == 1:
        return 1
    
    if (rows, cols) not in memo.keys():
        memo[(rows, cols)] = unique_paths(rows-1, cols, memo) + unique_paths(rows, cols-1, memo)
        # print(f'memo = {memo}')
        
    return memo[(rows, cols)]


if __name__ == '__main__':
    res = unique_paths(4, 5)    
    print(res)


"""
Returns:
    
35
"""