# Easy
# https://leetcode.com/problems/plus-one/
# Time Complexity: O(N)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        self.recursion_sol(digits, len(digits) - 1)
        # Iterative sol
        # for pos in range(len(digits) - 1, -1, -1):
        #     if digits[pos] < 9:
        #         digits[pos] += 1
        #         break
        #     else:
        #         if pos == 0:
        #             digits.append(0)
        #             digits[0] = 1
        #             break
        #         else:
        #             digits[pos] = 0
        return digits
        
    def recursion_sol(self, digits, place):
        if place >= 0:
            if digits[place] < 9:
                digits[place] = digits[place] + 1
            else:
                if place == 0:
                    digits.append(0)
                    digits[0] = 1
                else:
                    digits[place] = 0
                    self.recursion_sol(digits, place - 1)