# Medium
# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        #     TC: O(N)
        #     SC: O(N)
        if root:
            out = []
            stack = [root]
            while stack:
                curr = stack.pop()
                out.append(curr.val)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
            return out[::-1]
                    