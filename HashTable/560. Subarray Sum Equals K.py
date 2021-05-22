# Medium
# https://leetcode.com/problems/subarray-sum-equals-k/
# TC:O(n)
# SC:O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, sum = 0, 0
        d = {0: 1}
        for index, val in enumerate(nums):
            sum += val
            if sum - k in d:
                count += d[sum - k]
            d[sum] = d.get(sum, 0) + 1
        return count