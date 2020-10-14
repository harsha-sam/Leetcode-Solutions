# Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Time Complexity: O(N)
# Space Complexity: O(1)    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        gt = 1
        pivot = nums[0]
        for i in range(len(nums)):
            if nums[i] > pivot:
                pivot = nums[i]
                nums[gt], nums[i] = nums[i], nums[gt]
                gt += 1
        return gt