from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        suma = 0
        for i in range(k):
            suma += nums[i]
        max_sum = suma
        for i in range(k, len(nums)):
            suma += nums[i] - nums[i - k]
            max_sum = max(max_sum, suma)

        return max_sum / k
