class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def explore(candidates, target, comb, currentSum, startIdx, ans):
            if currentSum > target:
                return

            if currentSum == target:
                ans.append(comb[:])
                return

            for i in range(startIdx, len(candidates)):
                if currentSum + candidates[i] <= target:
                    comb.append(candidates[i])
                    currentSum += candidates[i]
                    explore(candidates, target, comb, currentSum, i, ans)
                    currentSum -= comb.pop()
                else:
                    break

        res = []
        candidates.sort()
        for i in range(len(candidates)):
            explore(candidates, target, [candidates[i]], candidates[i], i, res)
        return res
