from typing import List
from collections import OrderedDict


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1, d2 = dict(), dict()
        for i in range(len(list1)):
            d1[list1[i]] = i
        for i in range(len(list2)):
            d2[list2[i]] = i

        if len(d1) > len(d2):
            d1, d2 = d2, d1

        d = dict()

        for k in d1.keys():
            if k in d2.keys():
                if d1[k] + d2[k] in d:
                    d[d1[k] + d2[k]].append(k)
                else:
                    d[d1[k] + d2[k]] = list([k])

        return d[min(d.keys())]
