# Easy
# https://leetcode.com/problems/most-common-word/
# Time Complexity: O(N)
# Space Complexity: O(N)
# Solution Without Regex
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        d = {}
        new_para = ""
        for char in paragraph: # Also can use String.punctuation instead
            if char in ["!","?","'",",", ";","."]:
                new_para += ' '
            else:
                new_para += char.lower()
        words = new_para.split()
        for word in words:
            d[word] = d.get(word, 0) + 1
        for word in banned:
            d[word.lower()] = 0
        out = None
        for word, freq in d.items():
            if out is None:
                out = (word, freq)
            elif freq > out[1]:
                out = (word, freq)
        return out[0]

# Solution With Regex
# import re
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         d = {}
#         words = re.split(r"[!?',;. ]", paragraph)
#         print(words)
#         for word in words:
#             if word:
#                 word = word.lower()
#                 d[word] = d.get(word, 0) + 1
#         for word in banned:
#             d[word.lower()] = 0
#         out = None
#         for word, freq in d.items():
#             if out is None:
#                 out = (word, freq)
#             elif freq > out[1]:
#                 out = (word, freq)
#         return out[0]
