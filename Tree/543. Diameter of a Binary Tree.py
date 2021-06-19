# Easy
# https://leetcode.com/problems/diameter-of-binary-tree/
# TC: O(N)
# SC: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def diapair(root):
            if not root:
                return (-1, 0)
            l = diapair(root.left)  # Maximum diameter from left subtree
            r = diapair(root.right)  # Maximum diameter from right subtree
            f = l[0] + r[0] + 2
            h = max(l[0], r[0]) + 1
            max_dia = max(l[1], max(r[1], f))
            # max_diameter can either be from left, right or path from left deepest_node to right deepest_node
            return (h, max_dia)

        _, out = diapair(root)
        return out
