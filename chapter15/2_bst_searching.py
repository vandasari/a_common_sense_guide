"""
Binary Search Trees

Algorithm: Page 255
"""

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
       
        
# Try out
if __name__ == '__main__':
    # Build a simple tree:
    node1 = TreeNode(25)
    node2 = TreeNode(75)
    bst = TreeNode(50, node1, node2)
    
    print(f'Root: {bst.value}')
    print(f'Left child: {bst.leftChild.value}')
    print(f'Right child: {bst.rightChild.value}')
    
    print()
    
    # A list of values to be searched:
    searchVals = [25, 10, 75] 
    
    for val in searchVals:
        if val is not None:
            print(f'{val} is found' if bst.search(val, bst) else f'{val} is not found')
        
  