from typing import List
from collections import Counter


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        most_common = Counter(nums).most_common()
        my_most = []
        for k, v in most_common:
            if v == most_common[0][1]:
                my_most.append(k)
            else:
                break

        my_min = len(nums)
        for k in my_most:
            i, j = 0, len(nums) - 1
            while True:
                if nums[i] != k:
                    i += 1
                if nums[j] != k:
                    j -= 1

                if nums[i] == nums[j] == k:
                    my_min = min(my_min, len(nums[i:j + 1]))
                    break
        return my_min

    def findShortestSubArray2(self, nums: List[int]) -> int:
        count, left, right = {}, {}, {}
        for i in range(len(nums)):
            if nums[i] not in left: left[nums[i]] = i
            right[nums[i]] = i
            count[nums[i]] = count.get(nums[i], 0) + 1

        ans = len(nums)
        degree = max(count.values())

        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        return ans
