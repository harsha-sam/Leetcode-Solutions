from math import inf


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {name: i for i, name in enumerate(list1)}
        res = []
        mini = inf
        for i, name in enumerate(list2):
            if name in d:
                if d[name] + i < mini:
                    mini = d[name] + i
                    res = [name]
                elif d[name] + i == mini:
                    res.append(name)
        return res
