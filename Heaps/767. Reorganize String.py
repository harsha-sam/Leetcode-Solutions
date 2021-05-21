# Medium
# https://leetcode.com/problems/reorganize-string/
# TC:O(n log n)
# SC:O(n)

import heapq

class Solution:
    ''' Approach:
    1. Store Frequence of letters in a counter.
    2. Try alternatively placing the most common two letters everytime and decrement        its counter(Use priority queue to keep track)
    '''
    def reorganizeString(self, s: str) -> str:
        d = {}
        for letter in s:        
            d[letter] = d.get(letter, 0) + 1
        hq = []
        for key, val in d.items():
            heapq.heappush(hq, [-val, key])
        out = ""
        while len(hq) > 1:
            letter1 = heapq.heappop(hq)
            letter2 = heapq.heappop(hq)
            out += letter1[1] + letter2[1]
            letter1[0], letter2[0] = letter1[0] + 1, letter2[0] + 1
            if letter1[0] < 0:
                heapq.heappush(hq, letter1)
            if letter2[0] < 0:
                heapq.heappush(hq, letter2)
        if len(hq) == 1:
            letter = heapq.heappop(hq)
            if -letter[0] > 1:
                return ""
            out += letter[1]
        return out
        