# Medium
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# TC: O(N**2)

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def generateStrings(curr, pos):
            result[0] = max(result[0], len(hash_map))
            if pos == len(arr):
                return
            newString = curr
            tillAdded = 0
            for index, char in enumerate(arr[pos]):
                if char in hash_map:
                    tillAdded = index
                    break
                else:
                    newString += char
                    hash_map[char] = 1
            else:
                tillAdded = len(arr[pos])
                generateStrings(newString, pos + 1)
            for i in range(tillAdded):
                del hash_map[arr[pos][i]]
            generateStrings(curr, pos + 1)

        result = [0]
        hash_map = {}
        generateStrings("", 0)
        return result[0]
