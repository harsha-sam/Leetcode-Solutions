# Medium
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Time Complexity: O(Log N)
# SC: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_pivot(nums):
            if not nums: 
                return -1
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if mid > 0 and nums[mid - 1] > nums[mid]:
                    return mid
                elif nums[low] <= nums[mid] and nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            return low         
        index = find_pivot(nums)
        if index != -1:
            return nums[index]