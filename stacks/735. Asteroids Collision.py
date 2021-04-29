# Medium
# https://leetcode.com/problems/asteroid-collision/
# TC:O(N)
# SC:O(N)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for curr in asteroids:
            while stack and curr < 0 < stack[-1]:
                if -curr > stack[-1]:
                    stack.pop()
                    continue
                elif -curr == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(curr)
        return stack