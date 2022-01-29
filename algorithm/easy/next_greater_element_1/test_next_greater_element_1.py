from unittest import TestCase
from next_greater_element_1 import Solution


class TestSolution(TestCase):
    def test_next_greater_element(self):
        s = Solution()
        nums1, nums2 = [2, 4], [1, 2, 3, 4]
        ans = s.nextGreaterElement(nums1, nums2)
        self.assertEqual([3, -1], ans)

    def test_next_greater_element2(self):
        s = Solution()
        nums1, nums2 = [4, 1, 2], [1, 3, 4, 2]
        ans = s.nextGreaterElement(nums1, nums2)
        self.assertEqual([-1, 3, -1], ans)
