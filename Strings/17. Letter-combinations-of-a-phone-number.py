# Medium
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Time Complexity: O(3^p * 4^q) where p = len(filtered_digits) who have 3 letter mapping and q = len(filtered_digits) who have 4 letter mapping. p + q = n (len(digits))
# Space Complexity: O(3^p * 4^q), Since we have to keep all solutions
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':["a", "b", "c"],
            '3':["d", "e", "f"],
            '4':["g", "h", "i"],
            '5':["j", "k", "l"],
            '6':["m", "n", "o"],
            '7':["p","q","r", "s"],
            '8':["t", "u", "v"],
            '9':["w", "x", "y", "z"]}
        
        if len(digits) == 0:
            return []

        i = 1
        l1 = d[digits[0]]
        while i < len(digits):
            l2 = d[digits[i]]
            curr = []
            for x in l1:
                for y in l2:
                    curr.append(x + y)
            l1 = curr
            i += 1   
        return l1
        