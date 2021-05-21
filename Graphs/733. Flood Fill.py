# DFS
# Easy
# https://leetcode.com/problems/flood-fill/
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image
        def recursive_dfs(image, sr, sc, newColor):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != color:
                return
            image[sr][sc] = newColor
            recursive_dfs(image, sr + 1, sc, newColor)
            recursive_dfs(image, sr - 1, sc, newColor)
            recursive_dfs(image, sr, sc + 1, newColor)
            recursive_dfs(image, sr, sc - 1, newColor)
        
        recursive_dfs(image, sr, sc, newColor)
        return image