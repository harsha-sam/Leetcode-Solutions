# https://leetcode.com/problems/group-anagrams/
# Medium
# Time Complexity: O(n * s log s) where n = len(list) and s = length of longest string in the list
# We can reduce the time complexity by counting sort
# Space Complexity: O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            word = ''.join(sorted(strs[i])) 
            d[word] = d.get(word, []) + [strs[i]]
        return d.values()    
        