from unittest import TestCase
from set_mismatch import Solution


class TestSolution(TestCase):
    def test_find_error_nums(self):
        s = Solution()
        data = [1, 2, 2, 4]
        x = s.findErrorNums(data)
        self.assertEqual([2, 3], x)

    def test_find_error_nums2(self):
        s = Solution()
        data = [1, 1]
        x = s.findErrorNums(data)
        self.assertEqual([1, 2], x)

    def test_find_error_nums3(self):
        s = Solution()
        data = [3, 2, 3, 4, 6, 5]
        x = s.findErrorNums(data)
        self.assertEqual([3, 1], x)

    def test_find_error_nums4(self):
        s = Solution()
        data = [1, 2, 3, 4, 8, 6, 7, 8]
        x = s.findErrorNums(data)
        self.assertEqual([8, 5], x)
