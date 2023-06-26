from collections import deque


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = deque([1, 1], 2)

        for i in range(1, n):
            cache.append(sum(cache))
        return cache[-1]
