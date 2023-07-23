class TrieNode:
    def __init__(self):
        self.a = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for i in word:
            if i not in current.a:
                current.a[i] = TrieNode()
            current = current.a[i]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for i in word:
            if i not in current.a:
                return False
            current = current.a[i]
        return current.endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for i in prefix:
            if i not in current.a:
                return False
            current = current.a[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)