from unittest import TestCase
from intersection_of_two_arrays import Solution


class TestSolution(TestCase):
    def test_intersection3(self):
        s = Solution()
        nums1, nums2 = [1, 2, 2, 1], [2, 2]
        self.assertEqual([2], s.intersection4(nums1, nums2))

    def test_intersection4(self):
        s = Solution()
        nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
        self.assertEqual([4, 9], s.intersection4(nums1, nums2))
