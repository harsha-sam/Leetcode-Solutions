# Medium
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            index = abs(num) - 1
            if nums[index] >= 1:
                nums[index] = -nums[index]
            else:
                res.append(index + 1)
        return res
                
                