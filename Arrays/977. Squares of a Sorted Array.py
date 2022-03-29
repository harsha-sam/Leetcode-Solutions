# Easy
# https://leetcode.com/problems/squares-of-a-sorted-array/

# TC: O(N)
# SC: O(1)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def binary_search(nums, target):
            l, h = 0, len(nums) - 1
            while l <= h:
                mid = (l + h) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    h = mid - 1
                else:
                    l = mid + 1
            if nums[mid] < target:
                mid += 1
            return mid

        get_zero = binary_search(nums, 0)
        res = []
        i, j = get_zero - 1, get_zero
        while i >= 0 and j < len(nums):
            if abs(nums[i]) < abs(nums[j]):
                res.append(nums[i] ** 2)
                i -= 1
            else:
                res.append(nums[j] ** 2)
                j += 1
        while i >= 0:
            res.append(nums[i] ** 2)
            i -= 1
        while j < len(nums):
            res.append(nums[j] ** 2)
            j += 1
        return res
