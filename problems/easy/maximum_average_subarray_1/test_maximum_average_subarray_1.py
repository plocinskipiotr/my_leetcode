from unittest import TestCase
from maximum_average_subarray_1 import Solution


class TestSolution(TestCase):
    def test_find_max_average(self):
        s = Solution()
        nums, k = [1, 12, -5, -6, 50, 3], 4
        x = s.findMaxAverage(nums, k)
        self.assertEqual(12.75, x)

    def test_find_max_average2(self):
        s = Solution()
        nums, k = [5], 1
        x = s.findMaxAverage(nums, k)
        self.assertEqual(5, x)

    def test_find_max_average3(self):
        s = Solution()
        nums, k = [5, 5, 5], 2
        x = s.findMaxAverage(nums, k)
        self.assertEqual(5, x)

    def test_find_max_average4(self):
        s = Solution()
        nums, k = [1, 2, 3, 4], 4
        x = s.findMaxAverage(nums, k)
        self.assertEqual(2.5, x)

    def test_find_max_average5(self):
        s = Solution()
        nums, k = [7, 4, 5, 8, 8, 3, 9, 8, 7, 6], 7
        x = s.findMaxAverage(nums, k)
        self.assertEqual(7, x)
