"""
Exercise 2
Time complexity: O(n)
"""

def merge(array1, array2):
    new_array = []
    
    array_1_pointer = 0
    array_2_pointer = 0
    steps = 0
    
    while array_1_pointer < len(array1) or array_2_pointer < len(array2):
        steps += 1
        
        if array_1_pointer >= len(array1):
            new_array.append(array2[array_2_pointer])
            array_2_pointer += 1
        elif array_2_pointer >= len(array2):
            new_array.append(array1[array_1_pointer])
            array_1_pointer += 1
        elif array1[array_1_pointer] < array2[array_2_pointer]:
            new_array.append(array1[array_1_pointer])
            array_1_pointer += 1
        else:
            new_array.append(array2[array_2_pointer])
            array_2_pointer += 1
            
    return new_array, steps


if __name__ == '__main__':    
    arr1 = [30, 60, 70, 80, 90, 100, 120]
    arr2 = [1, 2, 3, 4, 5]
    
    res, m = merge(arr1, arr2)
    print(res)
    print(f'steps = {m}')