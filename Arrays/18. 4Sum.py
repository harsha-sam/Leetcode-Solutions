# Medium
# https://leetcode.com/problems/4sum/solution/
# Using Hash Table


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d = {}
        for i in range(len(nums)): # n ^ 2
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j] 
                if s in d:
                    d[s].append((i, j))
                else:
                    d[s] = [(i, j)]
        res = []         
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j] 
                if target - s in d:
                    for x, y in d[target - s]:
                        if i != x and j != y and i != y and j != x:
                            quad = sorted([nums[i], nums[j], nums[x], nums[y]])
                            if quad not in res:                                    
                                res.append(quad)
        return res