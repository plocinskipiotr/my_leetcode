from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        lst = list()
        for i in nums2:
            if i in s and i not in lst:
                lst.append(i)
        return lst

    def binary_search(self, item, nums2):
        l = 0
        r = len(nums2) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums2[mid] == item:
                return True
            if nums2[mid] > item:
                r = mid - 1
            else:
                l = mid + 1
        return False

    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        lst = list()
        for i in nums1:
            if self.binary_search(i, nums2) and i not in lst:
                lst.append(i)
        return lst

    def intersection4(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i = j = 0
        lst = list()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j] and nums1[i] not in lst:
                lst.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return lst
