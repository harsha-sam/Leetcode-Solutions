# Medium
# https://leetcode.com/problems/container-with-most-water/
# https://www.geeksforgeeks.org/container-with-most-water/
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            if height[l] <= height[r]:
                area = height[l] * (r - l)
                l += 1
            else:
                area = height[r] * (r - l)
                r -= 1
            if area > max_area:
                max_area = area
        return max_area