from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        max_index, sec_max_value = 0, -1
        for i in range(1, len(nums)):
            if nums[i] > nums[max_index]:
                sec_max_value = nums[max_index]
                max_index = i

            else:
                if nums[i] > sec_max_value:
                    sec_max_value = nums[i]

        result = max_index if nums[max_index] >= 2 * sec_max_value else -1

        return result
