# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            index = abs(num) - 1
            if nums[index] > 0 :
                nums[index] = -nums[index]
        out = []
        for i, num in enumerate(nums):
            if num > 0:
                out.append(i + 1)
        return out