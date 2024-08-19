"""
Exercise 4 - Autocorrect
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def search(self, word):
        currentNode = self.root
        
        for char in word:
            # If the current node has child key with current character:
            if currentNode.children.get(char):
                # Follow the child node:
                currentNode = currentNode.children[char]
            else:
                # If the current character isn't found among the current
                # node's children, our search word must not be in the trie:
                return None
            
        return currentNode
    
    
    def insert(self, word):
        currentNode = self.root
        
        for char in word:
            # If the current node has child key with current character:
            if currentNode.children.get(char):
                # Follow the child node:
                currentNode = currentNode.children[char]
            else:
                # If the current character isn't found among the current node's
                # children, we add the character as a new child node:
                newNode = TrieNode()
                currentNode.children[char] = newNode
                
                # Follow this new node:
                currentNode = newNode
                
        # After inserting the entire word into the trie, we add a * key at the end:
        currentNode.children['*'] = None
        
        
    def collectAllWords(self, node=None, word='', words=[]):
        """
        This method accepts three arguments: 
            - node: we're collecting words from node's descendants.
            - word: begins as empty string and we add characters to it as
            we move through the trie.
            - words: begins as an empty array and by the end of the function 
            will contain all the words from the trie.
        """
        
        # The current node is the node passed in as the 1st parameter, or the
        # root node if none is provided:
        currentNode = node or self.root
               
        # We iterate through all the current node's children hash table. Note that
        # the key is always a single-character string and the value is another instance of TrieNode:
        for key, childNode in currentNode.children.items():
            # Base case: if the current key is *, it means we hit the end of  
            # a complete word, so we can add it to our words array:
            if key == '*':
                words.append(word)
            else: # If we're still in the middle of a word,
                # we recursively traverse the trie and collect the words as we go:
                self.collectAllWords(childNode, word+key, words)
                
        return words
    
    
    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        
        if not currentNode:
            return None
        
        return self.collectAllWords(currentNode)
    
    
    def traverse(self, node=None):
        currentNode = node or self.root
        
        for key, childNode in currentNode.children.items():
            print(key)
            if key != '*':
                self.traverse(childNode)
        
    
    def autocorrect(self, word):
        currentNode = self.root
        
        wordFoundSoFar = ''
        
        for char in word:
            if currentNode.children.get(char):
                wordFoundSoFar += char
                currentNode = currentNode.children.get(char)
            else:
                return wordFoundSoFar + self.collectAllWords(currentNode)[0]
            
        return word
        
    
if __name__ == '__main__':
    inputStrings = ['tag', 'tank', 'tap', 'today', 'total', 'well', 'went']       
    
    t = Trie()
    
    for i in inputStrings:
        t.insert(i)
    
    misspelled = ['tas', 'weli']
    
    for c in misspelled:
        print(t.autocorrect(c))
    

        