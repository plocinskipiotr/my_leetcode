from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = Counter(nums)

        suma = 0
        for k in d.keys():
            if (k + 1) in d.keys():
                suma = max(suma, d[k] + d[k + 1])
        return suma
