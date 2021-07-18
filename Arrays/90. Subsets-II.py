# Medium
# https://leetcode.com/problems/subsets-ii/
# TC: O(2**N)
# SC: O(2**N)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def binary(num, length):
            s = ''
            while num > 0:
                s += str(num % 2)
                num //= 2
            return (length - len(s)) * '0' + s[::-1]

        nums.sort()
        hash_map = {}
        for i in range(2 ** len(nums)):
            bini = binary(i, len(nums))
            subset = []
            for i in range(len(nums)):
                if bini[i] == '1':
                    subset.append(nums[i])
            subset = tuple(subset)
            if not subset in hash_map:
                hash_map[subset] = True
        return hash_map.keys()
