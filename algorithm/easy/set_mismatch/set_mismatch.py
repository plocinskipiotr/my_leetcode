from typing import List
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        x = c.most_common(1)[0][0]
        lst = [x]
        for i in range(len(nums)):
            if (i + 1) not in c.keys():
                lst.append((i + 1))
        return lst
