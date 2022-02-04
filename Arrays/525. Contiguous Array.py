# https://leetcode.com/problems/contiguous-array/
# Medium
# TC: O(N)
# SC: O(N)

# Approach: using prefixsum
# Consider all 0 numbers as -1
# Case 1: When prefix sum is 0, then till that index we have equal pairs of 1's and 0's
# Case 2: Store prefix sum and indices as keys and values. When we encounter a prefix sum which is already there in hash map then we can say that from that already existing index in hash map to current index we have equal pairs of 1's and 0's.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        currSum, res = 0, 0
        hashSum = {}
        for index, num in enumerate(nums):
            if num == 0:
                currSum += -1
            else:
                currSum += 1
            if currSum == 0:
                res = max(res, index + 1)
            elif currSum in hashSum:
                res = max(index - hashSum[currSum], res)
            else:
                hashSum[currSum] = index
        return res
