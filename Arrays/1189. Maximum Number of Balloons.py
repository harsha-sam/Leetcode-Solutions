from collections import Counter
from math import inf


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        frq = Counter(text)
        min_count = inf
        for char in "balon":
            if char not in frq:
                return 0
            occurences = frq[char] // 2 if char in "lo" else frq[char]
            min_count = min(min_count, occurences)
        return min_count
