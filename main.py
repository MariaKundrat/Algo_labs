class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            node = current.children.get(char)
            if node is None:
                node = TrieNode()
                current.children.update({char: node})
            current = node
        current.end_of_string = True

    def search(self, word):
        current = self.root
        for char in word:
            node = current.children.get(char)
            if node is None:
                return False
            current = node
        if current.end_of_string is True:
            return True
        return False

    def search_prefix(self, prefix):
        current = self.root
        for char in prefix:
            node = current.children.get(char)
            if node is None:
                return False
            current = node
        return True


trie = Trie()
patterns = ["abc", "abk", "abcd", "mar", "rat", "rats"]
for pattern in patterns:
    trie.insert(pattern)
print(trie.search("rat"))
print(trie.search_prefix("rat"))
