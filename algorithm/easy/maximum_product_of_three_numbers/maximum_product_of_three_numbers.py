from functools import reduce
from typing import List
import heapq


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        if nums[-1] < 0 and nums[-2] < 0:
            return max(nums[-1] * nums[-2] * nums[0], nums[0] * nums[1] * nums[2])
        else:
            return reduce(lambda x, y: x * y, nums[:3])

    def maximumProductHeap(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        largest = heapq.nlargest(3, nums)
        smallest = heapq.nsmallest(2, nums)
        return max(largest[0] * largest[1] * largest[2], smallest[0] * smallest[1] * largest[0])
