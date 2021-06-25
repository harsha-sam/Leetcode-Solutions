# Medium
# https://leetcode.com/problems/max-consecutive-ones-iii/
# TC: O(N)
# SC: O(1)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        maxi = 0
        n = len(nums)
        while j < n:
            while k > 0 and j < n:
                if nums[j] == 0:
                    k -= 1
                j += 1
            while k == 0 and j < n and nums[j] == 1:
                j += 1
            while i < n and k == 0:
                maxi = max(maxi, j - i)
                if nums[i] == 0:
                    k += 1
                i += 1
        if j >= n and k > 0 and maxi == 0:
            maxi = max(maxi, j - i)
        return maxi
