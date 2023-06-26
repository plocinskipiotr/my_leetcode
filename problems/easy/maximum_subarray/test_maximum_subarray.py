from unittest import TestCase
from maximum_subarray import Solution


class TestSolution(TestCase):
    def test_max_sub_array_0(self):
        s = Solution()
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        sum = s.maxSubArray(nums)
        self.assertEqual(sum, 6)

    def test_max_sub_array_1(self):
        s = Solution()
        nums = [1]
        sum = s.maxSubArray(nums)
        self.assertEqual(sum, 1)

    def test_max_sub_array_2(self):
        s = Solution()
        nums = [5, 4, -1, 7, 8]
        sum = s.maxSubArray(nums)
        self.assertEqual(sum, 23)

    def test_max_sub_array_3(self):
        s = Solution()
        nums = [-2, -5, -1, -4, -3, -10, -3, -7]
        sum = s.maxSubArray(nums)
        self.assertEqual(sum, -1)
