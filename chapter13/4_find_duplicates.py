"""
Sorting as a Key to Other Algorithms

Algorithm: Page 223
Time complexity: O(n x log(n)) 

Python's sorted() function uses Timsort algorithm, which is a combination of 
merge sort and insertion sort. It has the time complexity of O(n log(n)).

sorted: O(n log(n))
loop: O(n)

Thus, the following function has time complexity O(n log(n)).
"""

def hasDuplicates(array):
    array = sorted(array) # Python implements Timsort for its sorted function
    
    for i in range(len(array)):
        if array[i] == array[i+1]:
            return True
        
    return False


if __name__ == '__main__':
    arr = [5, 9, 3, 2, 4, 5, 6]
    res = hasDuplicates(arr)
    print(res)




