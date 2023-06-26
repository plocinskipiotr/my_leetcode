from unittest import TestCase

from merge_sorted_array import Solution


class TestSolution(TestCase):
    def test_merge_0(self):
        s = Solution()
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        m = n = 3

        s.merge(nums1, m, nums2, n)

        self.assertEqual([1, 2, 2, 3, 5, 6], nums1)

    def test_merge_01(self):
        s = Solution()
        nums1 = [1, 6, 0, 0]
        nums2 = [5, 7]
        m = 2
        n = 2

        s.merge(nums1, m, nums2, n)

        self.assertEqual([1, 5, 6, 7], nums1)

    def test_merge_03(self):
        s = Solution()
        nums1 = [5,0]
        nums2 = [2]
        m = 1
        n = 1

        s.merge(nums1, m, nums2, n)

        self.assertEqual([2,5], nums1)

    def test_merge_05(self):
        s = Solution()
        nums1 = [5,5,0,0]
        nums2 = [2,2]
        m = 2
        n = 2

        s.merge(nums1, m, nums2, n)

        self.assertEqual([2,2,5,5], nums1)


    def test_merge_04(self):
        s = Solution()
        nums1 = [0]
        nums2 = [1]
        m = 0
        n = 1

        s.merge(nums1, m, nums2, n)

        self.assertEqual([1], nums1)

