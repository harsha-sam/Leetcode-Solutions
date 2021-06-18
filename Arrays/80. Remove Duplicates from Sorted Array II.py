# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# TC: O(N)
# SC: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        pivot = nums[0]
        l, i = 1, 1
        while i < len(nums):
            if nums[i] > pivot:
                nums[l], nums[i] = nums[i], nums[l]
                pivot = nums[l]
                l += 1
            elif nums[i] == pivot and (l - 2 < 0 or nums[l - 2] != pivot):
                nums[l], nums[i] = nums[i], nums[l]
                pivot = nums[l]
                l += 1
            i += 1
        return l
