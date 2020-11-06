# Medium
# Refer https://www.byte-by-byte.com/inordertraversal/?utm_source=optin_carrot&utm_medium=pdf&utm_campaign=50questions
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #     TC: O(N)
    #     SC: O(N)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def add_to_left(stack, n):
            while n:
                stack.append(n)
                n = n.left
                
        stack = []
        out = []
        add_to_left(stack, root)
        while stack:
            curr = stack.pop()
            out.append(curr.val)
            add_to_left(stack, curr.right)
        return out
            
        
                