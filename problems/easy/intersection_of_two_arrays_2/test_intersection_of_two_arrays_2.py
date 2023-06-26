from unittest import TestCase
from intersection_of_two_arrays_2 import Solution


class TestSolution(TestCase):
    def test_intersect(self):
        s = Solution()
        nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
        x = s.intersect2(nums1, nums2)
