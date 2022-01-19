from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        i = 0
        lst = list()
        for j in range(len(nums)):
            if nums[j] - nums[j - 1] > 1:
                if i == j - 1:
                    lst.append(str(nums[i]))
                else:
                    lst.append(str(nums[i]) + '->' + str(nums[j - 1]))
                i = j

            if j == len(nums) - 1:
                if i == j:
                    lst.append(str(nums[i]))
                else:
                    lst.append(str(nums[i]) + '->' + str(nums[j]))
        return lst
