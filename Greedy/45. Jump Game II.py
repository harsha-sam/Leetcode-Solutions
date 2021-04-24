# Medium
# https://leetcode.com/problems/jump-game-ii/
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Approach: 
        1) For every element in the array, Find the index at which it can reach by 
           taking the longest jump (i.e curr_index + element). Store these in an 
           array.
           [2, 4, 5, 1, 1, 1, 1, 1]
           reachable = [0 + 2, 1 + 4, 2 + 5, 3 + 1, 4 + 1, 5 + 1, 6 + 1, 7 + 1]
           = [2, 5, 7, 4, 5, 6, 7, 8]

       Note: There may be elements in the array reachable which are greater than 
       last index (i.e destination). Substitue last index at those positions.
       = [2, 5, 7, 4, 5, 6, 7, 8 (violates as 8 > last index which is 7, 
       substitute by 7)]
       Now reachable : [2, 5, 7, 4, 5, 6, 7, 7]

        2) Now,for every index i in reachable find the index of next maximum 
        reachable position within the range of reachable[i]. This the best move, we 
        are going to take, so update i = index of next maximum reachable pos. 
        There may be a case, where i can get unchanged if i is only greater in the 
        current range, then change i to point at reachable[i]

        3) Count till i reaches last index.

        4) Finally, Count is the minimum number of jumps required to reach last 
        index.

        Walkthrough for above example:

        reachable : [2, 5, 7, 4, 5, 6, 7, 7]

        i = 0
        index of next_maximum_reachable position from (0, reachable[0]) -> (0, 2) =2 
        (because reachable[2] = 7 and it is greater)
        so, update i = 2

        repeat from i = 2
        index of next_maximum_reachable position from (2, reachable[2]) -> (0, 7) = 
        0 (because reachable[2] is only maximum)
        Now in this case, where i is unchanged update i to point at reachable[i]
        so, i = reachable[2] = 7

        Now, i = last_index and we took two jumps to reach end

        '''
        # We can reduce the space complexity by just modifying the nums array,
        # instead of creating a new array to_indices

        # to_indices = []
        for i, num in enumerate(nums):
            # to_indices.append(min(i + num, len(nums) - 1))
            nums[i] = min(i + num, len(nums) - 1)

        def get_next_max(curr_max_index, lis, end):
            for i in range(curr_max_index + 1, end + 1):
                if lis[i] > lis[curr_max_index]:
                    curr_max_index = i
            return curr_max_index

        i, c = 0, 0
        while i < len(nums) - 1:
            temp = i
            i = get_next_max(i, nums, nums[i])
            if i == temp:
                i = nums[i]
            c += 1
        return c
