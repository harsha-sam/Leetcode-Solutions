# Easy
# https://leetcode.com/problems/sum-of-left-leaves/
# TC: O(N)
# SC: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def solve(node, isLeftBranch):
            nonlocal leftSum
            if not node:
                return
            if isLeftBranch and node.left is None and node.right is None:
                leftSum += node.val
            solve(node.left, True)
            solve(node.right, False)

        leftSum = 0
        solve(root, False)
        return leftSum
