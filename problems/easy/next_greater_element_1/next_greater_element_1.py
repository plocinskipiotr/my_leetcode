from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = list()
        hashmap = {}
        for i in nums2:
            while len(stack) > 0 and i > stack[-1]:
                hashmap[stack.pop()] = i
            else:
                stack.append(i)

        return list(map(lambda x: hashmap.get(x, -1), nums1))
