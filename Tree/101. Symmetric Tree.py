# Easy
# https://leetcode.com/problems/symmetric-tree/
# TC : O(N)
# SC : O(N)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recursive_check(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return (node1.val == node2.val) and recursive_check(node1.left, node2.right) and recursive_check(node1.right, node2.left)
        
        return recursive_check(root, root)