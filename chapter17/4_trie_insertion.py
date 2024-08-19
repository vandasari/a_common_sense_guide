"""
Algorithm: page 319

Time complexity: O(k)
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
        currentNode.children["*"] = None


if __name__ == "__main__":
    # Investigate trie insertion:
    test = Trie()
    test.insert("cat")

    print(test.root.children)
    print(test.root.children.get("c").children)
    print(test.root.children.get("c").children.get("a").children)
    print(test.root.children.get("c").children.get("a").children.get("t").children)

    print()

    # Try out trie search
    t = Trie()
    inputStrings = [
        "cat",
        "can",
        "core",
        "ceiling",
        "geek",
        "rush",
        "rusty",
        "ruin",
        "rain",
    ]
    queryStrings = ["geek", "run", "cat"]

    # inputStrings = ['ace', 'act', 'bad', 'bake', 'bat', 'batter', 'cab', 'cat']
    # queryStrings = ['cat', 'butter', 'ace']

    for w in inputStrings:
        t.insert(w)

    print("-- Root node: --")
    for i in t.root.children:
        print(i, end=" ")

    print("\n")

    for q in queryStrings:
        if t.search(q):
            print(f'query "{q}" is present in the table')
        else:
            print(f'query "{q}" is not found')
