# Medium
# https://leetcode.com/problems/h-index/

# TC : O(n log n)
# SC : O(1)

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if i + 1 >= citations[i]:
                if i + 1 == citations[i]:
                    return i + 1
                return i
        return i + 1
