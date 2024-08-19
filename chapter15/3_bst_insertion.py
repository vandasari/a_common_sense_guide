"""
Binary Search Trees - Insertion

Algorithm: Page 258--259
Time complexity: O(log n)
"""

import timeit


class TreeNode:
    def __init__(self, val, left=None, right=None):
        # Initialize a tree node with a value:
        self.value = val
        self.leftChild = left
        self.rightChild = right
        
        
    def search(self, searchValue, node):
        # Base case: if the node does not exist or we've found the value we're looking for:
        if node is None or node.value == searchValue:
            return node
        
        # If the value is less than the current node, perform search on the left child:
        elif searchValue < node.value:
            return self.search(searchValue, node.leftChild)
        
        # If the value is greater than the current node, perform search on the right child:    
        else: # searchValue > node.value
            return self.search(searchValue, node.rightChild)
              
        
    def insert(self, data, node):
        if data < node.value:
            if node.leftChild is None:
                node.leftChild = TreeNode(data)
            else:
                self.insert(data, node.leftChild)
                
        elif data > node.value:
            if node.rightChild is None:
                node.rightChild = TreeNode(data)
            else:
                self.insert(data, node.rightChild)

        
# Try out
if __name__ == '__main__':
    # Build a simple tree:    
    bst = TreeNode(50)
    
    values = [25, 75, 10, 33, 56, 89, 4, 11, 30, 40, 52, 61, 82, 95]
    
    for val in values:
        bst.insert(val, bst)
    
    print(f'Root: {bst.value}')
    print(f'Left child: {bst.leftChild.value}')
    print(f'Right child: {bst.rightChild.value}')
    print(f'Left-left child: {bst.leftChild.leftChild.value}')
    print(f'Left-right child: {bst.leftChild.rightChild.value}')
    print(f'Right-left child: {bst.rightChild.leftChild.value}')
    print(f'Right-right child: {bst.rightChild.rightChild.value}')
    
    print()
    
    # Benchmarking
    
    bm = TreeNode(50)
    bm.insert(25, bm)
    bm.insert(75, bm)
    bm.insert(10, bm)
    bm.insert(33, bm)
    bm.insert(89, bm)
    
    print('BST:', timeit.timeit('[func(56, bm) for func in (bm.insert, )]', globals=globals(), number=1), 'sec')
    
    arr = [10, 25, 33, 50, 75, 89]
    
    print('Array:', timeit.timeit('[func(4, 56) for func in (arr.insert, )]', globals=globals(), number=1), 'sec')
    
    