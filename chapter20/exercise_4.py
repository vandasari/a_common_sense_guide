"""
Exercise 4 - Recognizing Patterns

Time complexity: O(n)
"""


def greatestProduct(array):
    greatest_number = float('-inf')
    second_to_greatest_number = float('-inf')
    
    lowest_number = float('inf')
    second_to_lowest_number = float('inf')
    
    for number in array:
        if number >= greatest_number:
            second_to_greatest_number = greatest_number
            greatest_number = number
        elif number > second_to_greatest_number:
            second_to_greatest_number = number
            
        if number <= lowest_number:
            second_to_lowest_number = lowest_number
            lowest_number = number
        elif number > lowest_number and number < second_to_lowest_number:
            second_to_lowest_number = number
            
    greatest_product_from_two_highest = greatest_number * second_to_greatest_number
    
    greatest_product_from_two_lowest = lowest_number * second_to_lowest_number
    
    if greatest_product_from_two_highest > greatest_product_from_two_lowest:
        return greatest_product_from_two_highest
    else:
        return greatest_product_from_two_lowest



if __name__ == '__main__':
    
    arr = [-5, -4, -3, 0, 3, 4]
    # arr = [8, 2, 3, 9, 4, 7, 5, 0, 6]
    # arr = [0, 1, 3, 4, 5, 6]
    
    print(greatestProduct(arr))
    
