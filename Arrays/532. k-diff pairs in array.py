# Medium
# https://leetcode.com/problems/k-diff-pairs-in-an-array/submissions/

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = {}
        out = 0
        for num in nums:
            counter[num] = counter.get(num, 0) + 1 
        if k > 0:
            for num in counter.keys():
                if num + k in counter:
                    out += 1    
        else:
            for num in counter.keys():
                if counter[num] > 1:
                    out += 1
        return out