from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        suma = 0
        for i in range(0, len(nums), 2):
            suma += nums[i]
        return suma
