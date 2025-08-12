# Monotonic stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                lesser_index = stack.pop()
                res[lesser_index] = i - lesser_index
            stack.append(i)

        while stack:
            res[stack.pop()] = 0

        return res
