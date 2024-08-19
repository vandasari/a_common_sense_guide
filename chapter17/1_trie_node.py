"""
Algorithm: page 307
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        
        
p = {'a': TrieNode(), 'b': TrieNode(), 'c': TrieNode()}
print(p)