# https://leetcode.com/problems/word-search-ii/
# Hard
class TrieNode:
    def __init__(self, letter='/'):
        self.letter = letter
        self.children = {}
        self.ending = 0
        self.completeWord = ''


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for letter in word:
            if not letter in curr.children:
                curr.children[letter] = TrieNode(letter)
            curr = curr.children[letter]
        curr.ending += 1
        curr.completeWord = word


class Solution(object):
    def findWords(self, board, words):
        def dfs(i, j, node, board, words_found):
          if node.ending:
              words_found.append(node.completeWord)
              node.ending -= 1
          if i >= len(board) or i < 0 or j < 0 or j >= len(board[0]):
              return
          if board[i][j] == '$':
              return
          char = board[i][j]
          if char in node.children:
              next_node = node.children[char]
              board[i][j] = '$'
              dfs(i + 1, j, next_node, board, words_found)
              dfs(i - 1, j, next_node, board, words_found)
              dfs(i, j + 1, next_node, board, words_found)
              dfs(i, j - 1, next_node, board, words_found)
              board[i][j] = char

        t = Trie()
        for word in words:
          t.insert(word)
        words_found = []
        for i in range(len(board)):
          for j in range(len(board[0])):
            dfs(i, j, t.root, board, words_found)
        return words_found
