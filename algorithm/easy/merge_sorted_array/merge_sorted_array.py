class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        last = m + n - 1
        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[last] = nums2[j]
                j -= 1
            else:
                nums1[last] = nums1[i]
                i -= 1
            last -= 1

        if i < 0 and j >= 0:
            nums1[:last + 1] = nums2[:j + 1]