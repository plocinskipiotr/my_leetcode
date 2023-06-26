from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        all_sum = sum(nums)
        curr_sum = 0

        for i in range(len(nums)):
            if all_sum - nums[i] - curr_sum == curr_sum:
                return i
            curr_sum += nums[i]
        return -1