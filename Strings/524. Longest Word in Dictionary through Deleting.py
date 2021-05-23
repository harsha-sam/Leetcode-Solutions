# Medium
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
# TC: O(n * s) : n-> number of strings in d and s-> average string length
# SC: O(s) : s-> max string length that can be formed
import math

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:        
        max_len, out = -math.inf, ""
        for word in dictionary:
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == len(word) and ((j > max_len) or (j == max_len and word < out)):
                max_len = j
                out = word
        return out