from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        sum = 0
        for i in range(len(timeSeries) - 1):
            sum += min(timeSeries[i + 1] - timeSeries[i], duration)

        sum += duration
        return sum
