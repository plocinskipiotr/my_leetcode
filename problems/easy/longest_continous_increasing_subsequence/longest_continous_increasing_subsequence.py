from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_sub_len = sub_len = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                sub_len += 1
                max_sub_len = max(max_sub_len, sub_len)
            else:
                sub_len = 1
        return max_sub_len
