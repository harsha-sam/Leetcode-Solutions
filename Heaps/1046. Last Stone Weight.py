# Easy
# https://leetcode.com/problems/last-stone-weight/
# TC: O(n log n)
# SC: O(n)
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for index, val in enumerate(stones):
            stones[index] = -val
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, (y - x))
        if len(stones) == 1:
            return -stones[0]
        return 0