class TrieNode:
    def __init__(self, val=""):
        self.val = val
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not (char in curr.children):
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if not (char in curr.children):
                return False
            curr = curr.children[char]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if not (char in curr.children):
                return False
            curr = curr.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
