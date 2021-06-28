# Hard
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# TC: O(N log N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        q = deque([(root, 0)])
        d = {}
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                node, y = q.popleft()
                if y in d:
                    if level in d[y]:
                        d[y][level].append(node.val)
                    else:
                        d[y][level] = [node.val]
                else:
                    d[y] = {level: [node.val]}
                if node.left:
                    q.append((node.left, y - 1))
                if node.right:
                    q.append((node.right, y + 1))
            level += 1
        for col, col_data in d.items():
            for row in col_data:
                col_data[row].sort()
        ans = sorted(d.items(), key=lambda info: info[0])
        out = []
        for col, col_map in ans:
            row_data = []
            for row in col_map:
                row_data += col_map[row]
            out.append(row_data)
        return out
