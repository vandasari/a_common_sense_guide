"""
Binary Search Trees - Traversal

Algorithm: Page 273
Time complexity: O(n)
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
        
        
    def lift(self, node, nodeToDelete):
        if node.leftChild:
            node.leftChild = self.lift(node.leftChild, nodeToDelete)
            return node
        else:
            nodeToDelete.value = node.value
            return node.rightChild


    def delete(self, valueToDelete, node):
        if node is None:
            return None
        
        elif valueToDelete < node.value:
            node.leftChild = self.delete(valueToDelete, node.leftChild)
            return node
        
        elif valueToDelete > node.value:
            node.rightChild = self.delete(valueToDelete, node.rightChild)
            return node
        
        elif valueToDelete == node.value:
            if node.leftChild is None:
                return node.rightChild
            elif node.rightChild is None:
                return node.leftChild
            else:
                node.rightChild = self.lift(node.rightChild, node)
                return node 


    def inorderTraversal(self, node):
        if node is None:
            return
        
        self.inorderTraversal(node.leftChild)
        print(node.value, end='; ')
        self.inorderTraversal(node.rightChild)
        

        
# Try out
if __name__ == '__main__':
    # Build a simple tree:    
    bst = TreeNode(50)
    
    values = [25, 75, 10, 33, 56, 89, 4, 11, 30, 40, 52, 61, 82, 95]
    
    for val in values:
        bst.insert(val, bst)
    
    print(f'Root: {bst.value}')
    bst.inorderTraversal(bst)
    
    print('\n')
    
    bst.delete(50, bst)
    
    print(f'After deletion, root: {bst.value}')
    bst.inorderTraversal(bst)
    
    print('\n')
    
    books = TreeNode("Moby Dick")
    books.insert("Great Expectations", books)
    books.insert("Robinson Crusoe", books)
    books.insert("Alice in Wonderland", books)
    books.insert("Lord of the Flies", books)
    books.insert("Pride and Prejudice", books)
    books.insert("The Odyssey", books)
    
    books.inorderTraversal(books)