# 27. Remove Element
# https://leetcode.com/problems/remove-element/
# Easy

# Time Complexity : O(N)
#  Space Complexity: O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = len(nums) - 1
        l = 0
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        return r + 1