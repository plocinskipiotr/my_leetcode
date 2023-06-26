from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            x = abs(nums[i])
            nums[x - 1] = -1 * abs(nums[x - 1])

        lst = list()
        for i in range(len(nums)):
            if nums[i] > 0:
                lst.append(i + 1)

        return lst
