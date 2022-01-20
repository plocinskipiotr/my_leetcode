from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        j = 0
        for i in range(len(nums)):
            if nums[j] == 0 and nums[i] != 0:
                nums[j] = nums[i]
                nums[i] = 0
            if nums[j] != 0:
                j += 1
