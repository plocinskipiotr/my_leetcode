from typing import List
from collections import Counter


class Solution:
    def majorityElementDict(self, nums: List[int]) -> int:
        d = dict()
        for el in nums:
            if el in d:
                d[el] += 1
            else:
                d[el] = 1
        return max(d, key=d.get)

    def majorityElementDict2(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElementSorting(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElementVoting(self, nums: List[int]) -> int:

        el = nums[0]
        cnt = 0
        for i in nums:
            if cnt == 0:
                el = i

            if el == i:
                cnt += 1
            else:
                cnt -= 1
        return el
