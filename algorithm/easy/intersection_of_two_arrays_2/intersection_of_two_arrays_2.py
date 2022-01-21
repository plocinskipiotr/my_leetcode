from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        c = Counter(nums1)
        lst = list()
        for el in nums2:
            if el in c and c[el]:
                lst.append(el)
                c[el] = c[el] - 1
                # c.subtract([el])

        return lst

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i = j = 0
        lst = list()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                lst.append(nums1[i])
                i, j = i + 1, j + 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return lst
