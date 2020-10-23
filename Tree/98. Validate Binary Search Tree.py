# Medium
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(h)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.explore(root, -math.inf, math.inf) 
    
    def explore(self, node, mini, maxi):
        if node:
            if node.val <= mini or node.val >= maxi:
                return False
            if not self.explore(node.left, mini, node.val):
                return False
            if not self.explore(node.right, node.val, maxi):
                return False
        return True
    
            
            
        