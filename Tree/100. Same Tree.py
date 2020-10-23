# Easy
# https://leetcode.com/problems/same-tree/
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(tree height)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.helper(p, q)
    
#     Recursive Inorder Traversal check
    def helper(self, node1, node2):
        if node1 and not node2 or node2 and not node1:
            return False
        elif node1 and node2:
            if not self.helper(node1.left, node2.left):
                return False
            if node1.val != node2.val:
                return False
            if not self.helper(node1.right, node2.right):
                return False
        return True
        
        