from typing import List
from collections import Counter


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        sum = i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i, j, sum = i + 1, j + 1, sum + 1
            else:
                i += 1
        return sum
