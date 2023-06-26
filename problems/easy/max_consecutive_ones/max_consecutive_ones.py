from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max = 0
        curr = 0
        for j in range(len(nums)):
            if nums[j] == 1:
                curr += 1
            if nums[j] == 0:
                curr_max = max(curr_max, curr)
                curr = 0

        return max(curr, curr_max)
