# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, mini, maxi):
            if not node:
                return True
            return node and mini < node.val < maxi and helper(node.left, mini, node.val) and helper(node.right, node.val, maxi)

        return helper(root, -math.inf, math.inf)
