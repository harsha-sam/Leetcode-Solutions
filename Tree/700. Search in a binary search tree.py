# Easy
# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(log n)
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            if val >= root.val:
                root = root.right
            else:
                root = root.left
                
    