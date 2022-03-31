# Medium
# https://leetcode.com/problems/decode-the-slanted-ciphertext/

# TC: O(n)
# SC: O(1)
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        res = ''
        for j in range(cols):
            i = 0
            while i < rows and j < cols:
                index = cols * i + j
                res += encodedText[index]
                i += 1
                j += 1
        return res.rstrip()