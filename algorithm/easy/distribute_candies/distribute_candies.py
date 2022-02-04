from typing import List
from collections import Counter


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        c = set(candyType)
        she_can_eat = len(candyType) // 2
        number_of_types = len(c)
        return min(number_of_types, she_can_eat)
