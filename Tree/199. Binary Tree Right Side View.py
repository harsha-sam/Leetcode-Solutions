# Medium
# https://leetcode.com/problems/binary-tree-right-side-view/
# TC : O(N)
# SC : O(N)

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        out = []
        q = deque([root])
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            out.append(curr.val)
        return out