# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Time Complexity: O(N) 
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mini = prices[0]
        for price in prices[1:]:
            mini = min(mini, price)
            ans = max(ans, price - mini)
        return ans
