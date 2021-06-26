# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Hard
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# TC: O(N)
# SC: O(N)
from math import inf


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def pathSum(node):
            nonlocal maxi
            if not node:
                return 0
            left = max(0, pathSum(node.left))
            right = max(0, pathSum(node.right))
            maxi = max(maxi, left + right + node.val)
            return max(left, right) + node.val

        maxi = -inf
        pathSum(root)
        return maxi
