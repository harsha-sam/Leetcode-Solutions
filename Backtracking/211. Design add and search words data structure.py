class TrieNode:
    def __init__(self, text=' '):
        self.text = text
        self.children = {}
        self.isword = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode(letter)
            curr = curr.children[letter]
        curr.isword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(i, curr):
            if i == len(word):
                return curr.isword
            if word[i] == '.':
                for child in curr.children:
                    if dfs(i + 1, curr.children[child]):
                        return True
                return False
            else:
                if word[i] not in curr.children:
                    return False
                return dfs(i + 1, curr.children[word[i]])
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
