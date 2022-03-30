# Medium
# https://leetcode.com/problems/number-of-matching-subsequences/

# Solution using Trie - Not space optimal
# class TrieNode:
#     def __init__(self, letter=''):
#         self.letter = letter
#         self.children = {}
#         self.isEnding = 0

# class Trie:
#     def __init__(self):
#         self.t = TrieNode()

#     def add_word(self, word):
#         curr = self.t
#         for letter in word:
#             if not letter in curr.children:
#                 curr.children[letter] = TrieNode(letter)
#             curr = curr.children[letter]
#         curr.isEnding += 1

# class Solution:
#     def numMatchingSubseq(self, s: str, words: List[str]) -> int:
#         root = Trie()
#         for w in words:
#             root.add_word(w)
#         ans = 0
#         queue = [(root.t, 0)]
#  #queue contains tuples (node, idx), where node is the last visited node on the current
# #branch, and idx indicates that so far the branch is a subsequence of s[:idx]
#         while queue:
#             curr, i = queue.pop()
#             for char in curr.children:
#                 for j in range(i, len(s)):
#                     if s[j] == char:
#                         node = curr.children[char]
#                         ans += node.isEnding
#                         queue.append((node, j + 1))
#                         break
#         return ans

# Solution Using Binary Search
# TC: O(M * K log n) K = max length of the strings in the words array;m = len of words array;n=len of s
# SC: O(N)
from bisect import bisect_right
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        hash_map = {}
        for i, letter in enumerate(s):
            if letter in hash_map:
                hash_map[letter].append(i)
            else:
                hash_map[letter] = [i]

        res = 0
        for word in words:
            curr = -1
            for char in word:
                if char in hash_map:
                    index = bisect_right(hash_map[char], curr)
                    if index == len(hash_map[char]):
                        break
                    curr = hash_map[char][index]
                else:
                    break
            else:
                res += 1
        return res
