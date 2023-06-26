from typing import List
from collections import deque


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if not k:
            return False

        hashmap = dict()
        i = 0
        for num in nums:

            if num not in hashmap.values():
                hashmap[i] = num
            else:
                return True

            i += 1
            if i == k:
                i = 0

        return False

    def containsNearbyDuplicateFIFO(self, nums: List[int], k: int) -> bool:

        d = deque(maxlen=k)
        for num in nums:
            if num in d:
                return True
            d.append(num)

        return False

    def containsNearbyDuplicateSet(self, nums: List[int], k: int) -> bool:

        hashmap = set()
        k = k if len(nums) > k else len(nums) - 1
        for i in range(len(nums)):

            if nums[i] in hashmap:
                return True

            hashmap.add(nums[i])

            if i >= k:
                hashmap.remove(nums[i - k])
