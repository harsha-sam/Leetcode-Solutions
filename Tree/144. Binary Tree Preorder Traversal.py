# Medium
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     TC: O(N)
#     SC: O(N)
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            out = [root.val]
            stack = []
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            while stack:
                curr = stack.pop()
                out.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
            return out
            
        