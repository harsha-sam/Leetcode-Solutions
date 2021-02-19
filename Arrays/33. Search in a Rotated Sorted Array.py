# Medium
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Time Complexity: O( log N)
# Space Complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums):
            if not nums: 
                return -1
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if mid > 0 and nums[mid - 1] > nums[mid]:
                    return mid
                elif nums[low] <= nums[mid] and nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            return low            
        
        pivot = find_pivot(nums)
        low = 0
        high = len(nums)
        while low <= high:
            mid = (low + high) // 2
            actual_index = (mid + pivot) % len(nums)
            if nums[actual_index] == target:
                return actual_index
            elif nums[actual_index] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1