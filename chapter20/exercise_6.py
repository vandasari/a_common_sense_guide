"""
Exercise 6 - Longest Consecutive Sequence

Time complexity: O(n)
"""


def longestSequence(array):
    ht = {i: True for i in array}
    
    greatest_sequence_length = 0
    
    for num in array:
        if (num - 1) not in ht:
            current_sequence_length = 1
            current_number = num
            
            while ht.get(current_number + 1) is not None:
                current_number += 1
                current_sequence_length += 1
                
                if current_sequence_length > greatest_sequence_length:
                    greatest_sequence_length = current_sequence_length
    
    return greatest_sequence_length



if __name__ == '__main__':
    
    arr = [10, 5, 12, 3, 55, 30, 4, 11, 2]
    # arr = [19, 13, 15, 12, 18, 14, 17, 11]
    
    print(longestSequence(arr))
       
 