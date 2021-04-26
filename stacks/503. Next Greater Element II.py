# Medium
# https://leetcode.com/problems/next-greater-element-ii/
# TC: O(N)
# SC: O(N)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums + nums
        stack = []
        out = [-1 for _ in nums]
        for index, num in enumerate(nums):
            while len(stack) and num > nums[stack[-1]]:
                out[stack.pop()] = num
            stack.append(index)
        return out[:len(nums) // 2]
