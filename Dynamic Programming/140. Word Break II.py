class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = [[] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    if i + len(w) == len(s):
                        memo[i].append(w)
                    else:
                        for formedWord in memo[i + len(w)]:
                            memo[i].append(w + " " + formedWord)
        return memo[0]
