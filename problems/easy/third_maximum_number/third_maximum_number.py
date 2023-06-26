from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        j, item = 0, nums[0]

        for i in range(len(nums)):
            if nums[i] != item:
                j += 1
                item = nums[i]
            if j == 2:
                return item
        return nums[0]

    def thirdMaxSet(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        return nums[2] if len(nums) > 2 else nums[0]
