class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        i = 1
        res = []
        while i + 1 < len(mountain):
            if mountain[i - 1] < mountain[i] > mountain[i + 1]:
                res.append(i)
                i += 2
            else:
                i += 1
        return res
