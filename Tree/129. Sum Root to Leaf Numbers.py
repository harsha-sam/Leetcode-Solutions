
# Medium
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
# Time complexity : O(N) we'll visit each node at most one time
# Space Complexity : O(Tree height) - tree height is where a leaf node exits and dfs can atmost recursively repeat upto that length

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root:
            return self.dfs_helper(root, root.val, 0)[0]
        return 0
    
    def dfs_helper(self, node, curr, out):
        if node.left is None and node.right is None:
            out += curr
        if node.left:
            curr = curr * 10 + node.left.val
            out, curr = self.dfs_helper(node.left, curr, out)
        if node.right:
            curr = curr * 10 + node.right.val
            out, curr = self.dfs_helper(node.right, curr, out)
        curr //= 10
        return out, curr
        
        