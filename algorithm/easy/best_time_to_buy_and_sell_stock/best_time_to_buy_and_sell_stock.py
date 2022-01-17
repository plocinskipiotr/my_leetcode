from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        curr_max = 0

        for el in prices[1:]:
            curr_min = min(el, curr_min)
            curr_max = max(el - curr_min, curr_max)

        return curr_max
