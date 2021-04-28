# Medium
# https://leetcode.com/problems/continuous-subarray-sum/

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    # Input: 23 2 4 6 7
    # Cum_sum  23 25 29 35 42
    # Hash_Map
    #         5 -> 0 2 3
    #         1 -> 1
    #         0 -> 4
    # Soln: [1->2, 1->3, 3, 1->4]
        hash_map = {}
        cum_sum = 0
        for index, num in enumerate(nums):
            cum_sum += num
            rem = cum_sum % k if k != 0 else cum_sum
            if rem == 0 and index > 0:
                return True
            elif rem in hash_map:
                if index - hash_map[rem] > 1:
                    return True
            else:
                hash_map[rem] = index
        return False