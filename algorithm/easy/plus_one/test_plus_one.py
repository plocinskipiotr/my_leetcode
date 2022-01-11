from unittest import TestCase

from plus_one import Solution


class TestSolution(TestCase):
    def test_plus_one_0(self):
        s = Solution()
        data = [8, 9, 9]
        x = s.plusOne(data)
        self.assertEqual([9, 0, 0], x)

    def test_plus_one_1(self):
        s = Solution()
        data = [8, 8, 8]
        x = s.plusOne(data)
        self.assertEqual([8, 8, 9], x)

    def test_plus_one_2(self):
        s = Solution()
        data = [9, 9, 9]
        x = s.plusOne(data)
        self.assertEqual([1, 0, 0, 0], x)

    def test_plus_one_3(self):
        s = Solution()
        data = [9]
        x = s.plusOne(data)
        self.assertEqual([1, 0], x)

    def test_plus_one_4(self):
        s = Solution()
        data = [5]
        x = s.plusOne(data)
        self.assertEqual([6], x)
