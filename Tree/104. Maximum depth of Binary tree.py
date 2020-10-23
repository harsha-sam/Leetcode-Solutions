# Easy
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity : O(N)
# Space Complexity : O(N)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.depth(root)
    
    def depth(self, node):
        if node:
            return max(self.depth(node.left), self.depth(node.right)) + 1
        return 0