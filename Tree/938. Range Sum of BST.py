# Easy
# https://leetcode.com/problems/range-sum-of-bst/
# TC:O(n)
# SC:O(n)

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node, range_sum):
            if not node:
                return 0
            if node.val < low:
                return dfs(node.right, range_sum)
            if node.val > high:
                return dfs(node.left, range_sum)
            return node.val + dfs(node.left, range_sum) + dfs(node.right, range_sum)
        return dfs(root, 0)