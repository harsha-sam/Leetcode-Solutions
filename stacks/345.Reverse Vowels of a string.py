# Easy
# https://leetcode.com/problems/reverse-vowels-of-a-string/
    
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        for letter in s:
            if letter in "aeiouAEIOU":
                stack.append(letter)
        word = ""
        for letter in s:
            if letter in "aeiouAEIOU":
                word += stack.pop()
            else:
                word += letter
        return word
                