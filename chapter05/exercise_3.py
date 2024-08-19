"""
Exercise 3

Time complexity: O(n) with 2n steps
"""
    
def double_then_sum(array):
    doubled_array = []
    
    for number in array:
        number *= 2
        doubled_array.append(number)
        
    _sum = 0
    
    for num in doubled_array:
        _sum += num
        
    return _sum

def double_then_sum_without_append(array):
    newarr = [0] * len(array)
    
    for i in range(len(array)):
        newarr[i] = array[i]*2
        
    _sum = 0
    
    for j in newarr:
        _sum += j
        
    return _sum


def double_then_sum_list_comprehension(array):
    doubled = [i*2 for i in array]
    _sum = 0
    
    for number in doubled:
        _sum += number
        
    return _sum


if __name__ == '__main__':
    arr = [4, 2, 7, 1, 3]
    
    res1 = double_then_sum(arr)
    res2 = double_then_sum_without_append(arr)
    res3 = double_then_sum_list_comprehension(arr)
    
    print(res1)
    print(res2)
    print(res3)
