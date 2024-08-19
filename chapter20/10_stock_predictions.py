"""
Greedy Algorithms - Stock Predictions

Algorithm: Page 425

Time complexity: O(n)
Auxiliary space: O(1)
"""

def increasing_triplet(array):
    lowest_price = array[0]
    middle_price = float('inf')
    
    for price in array:
        if price <= lowest_price:
            lowest_price = price
        elif price <= middle_price:
            middle_price = price
        else:
            return True
        
    return False
    
    


if __name__ == '__main__':
    arr = [5, 2, 8, 4, 3, 7]
    
    print(increasing_triplet(arr))