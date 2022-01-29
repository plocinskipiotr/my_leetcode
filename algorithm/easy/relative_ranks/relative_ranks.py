import heapq
from heapq import heapify, heappop
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = dict()
        lst_score = score.copy()
        lst_score = [-x for x in lst_score]
        heapify(lst_score)

        while lst_score:
            el = heappop(lst_score)
            if len(d) == 0:
                d[el] = 'Gold Medal'
            elif len(d) == 1:
                d[el] = 'Silver Medal'
            elif len(d) == 2:
                d[el] = 'Bronze Medal'
            else:
                d[el] = str(len(d) + 1)

        return [d[-x] for x in score]
