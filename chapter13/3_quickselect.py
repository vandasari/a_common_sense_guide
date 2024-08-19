"""
Quickselect

Algorithm: Page 221
Time complexity: O(n)
"""


class SortableArray:
    def __init__(self, array):
        self.array = array
        
    def partition(self, left_pointer, right_pointer):
        # We always choose the right-most element as the pivot.
        # We keep the index of the pivot for later use:
        pivot_index = right_pointer
        
        # We grab the pivot value itself:
        pivot = self.array[pivot_index]
        
        # We start the right pointer immediately to the left of the pivot
        right_pointer -= 1
        
        while True:
            # Move the left pointer to the right as long as it points to
            # a value that is less that the pivot:
            while self.array[left_pointer] < pivot:
                left_pointer += 1
                
            # Move the right pointer to the left as long as it points to
            # a value that is greater than the pivot:
            while self.array[right_pointer] > pivot:
                right_pointer -= 1
                
            # We've now reached the point where we've stopped moving both the
            # left and right pointers.
            
            # We check whether the left pointer has reached or gone beyond
            # the right pointer. If it has, we break out of the loop so we
            # can swap the pivot later on:
            if left_pointer >= right_pointer:
                break
            # If the left pointer is still to the left of the right pointer,
            # we swap the values of the left and right pointers: 
            else:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]
                
                # We move the left pointer over to the right, gearing up for
                # the next round of left and right pointer movements:
                left_pointer += 1
                
        # As the final step of the partition, we swap the value of the left pointer with the pivot:
        self.array[left_pointer], self.array[pivot_index] = self.array[pivot_index], self.array[left_pointer]
        
        # We return the left pointer for the sake of the quicksort method:
        return left_pointer
   
    
    def quicksort(self, left_index, right_index):
        # Base case: the subarray has 0 or 1 elements:
        if right_index - left_index <= 0:
            return
        
        # Partition the range of elements and grab the index of the pivot:
        pivot_index = self.partition(left_index, right_index)
        
        # Recursively call this quicksort method on whatever is to the left of
        # the pivot:
        self.quicksort(left_index, pivot_index - 1)
        
        # Recursively call this quicksort method on whatever is to the left of
        # the pivot:
        self.quicksort(pivot_index + 1, right_index)
  
          
    def quickselect(self, kth_lowest_value, left_index, right_index):
        # If we reach a base case - that is, that the subarray has one cell, we
        # know we've found the value we're looking for:
        if right_index - left_index <= 0:
            return self.array[left_index]
        
        # Partition the array and grab the index of the pivot:
        pivot_index = self.partition(left_index, right_index)
        
        # If what we're looking for is to the left of the pivot:
        if kth_lowest_value < pivot_index:
            # Recursively perform quickselect on the subarray to the left of
            # the pivot:
            self.quickselect(kth_lowest_value, left_index, pivot_index - 1)
        # If what we're looking for is to the right of the pivot:
        elif kth_lowest_value > pivot_index:
            # Recursively perform quickselect on the subarray to the right of
            # the pivot:
            self.quickselect(kth_lowest_value, pivot_index + 1, right_index)
        # If kth_lowest_value == pivot_index:
        else:
            # If after the partition, the pivot position is in the same spot
            # as the kth lowest value, we've found the value we're looking for:
            return self.array[pivot_index]
    

if __name__ == '__main__':
    import random
    random.seed(10)
    
    arr1 = [0, 50, 20, 10, 60, 30]
    print(arr1)
    sortarr1 = SortableArray(arr1)
    # To find the second-to-lowest value of an unsorted array
    sortarr1.quickselect(1, 0, len(arr1) - 1)
    print(arr1)
    
    print()
    
    arr2 = random.sample(range(0, 21), 10)
    print(arr2)
    sortarr2 = SortableArray(arr2)
    # To find the fourth-to-lowest value of an unsorted array
    sortarr2.quickselect(3, 0, len(arr2) - 1)
    print(arr2)
    

"""
Input arguments
- The first argument: the position we’re looking for, starting at index 0. 
  E.g.: 1 to represent the second-to-lowest value, 4 to represent the fifth-to-lowest value
- The second argument: the left index of the array.
- The third argument: the right index of the array.
"""