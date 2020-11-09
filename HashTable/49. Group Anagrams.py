# https://leetcode.com/problems/group-anagrams/
# Medium
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            word = ''.join(sorted(strs[i])) 
            d[word] = d.get(word, []) + [strs[i]]
        return d.values()    
        