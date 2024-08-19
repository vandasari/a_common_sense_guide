"""
Binary Search Trees

Algorithm: Page 251
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        # Initialize a tree node with a value:
        self.value = val
        self.leftChild = left
        self.rightChild = right
        
        
        
if __name__ == '__main__':
    # Build a simple tree:
    node1 = TreeNode(25)
    node2 = TreeNode(75)
    root = TreeNode(50, node1, node2)
    
    print(f'Root: {root.value}')
    print(f'Left child: {root.leftChild.value}')
    print(f'Right child: {root.rightChild.value}')
  
    
"""
Returns:
    
Root: 50
Left child: 25
Right child: 75   
"""