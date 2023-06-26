from unittest import TestCase
from pascal_triangle import Solution


class TestSolution(TestCase):
    def test_generate_4(self):
        s = Solution()
        nums = 5
        x = s.generate2(nums)
        self.assertEqual(x, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

    def test_generate(self):
        s = Solution()
        nums = 5
        x = s.generate(nums)
        self.assertEqual(x, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

    def test_generate_0(self):
        s = Solution()
        nums = 4
        x = s.generate2(nums)
        self.assertEqual(x, [[1],[1,1],[1,2,1],[1,3,3,1]])

    def test_generate_1(self):
        s = Solution()
        nums = 3
        x = s.generate2(nums)
        self.assertEqual(x, [[1],[1,1],[1,2,1]])

    def test_generate_2(self):
        s = Solution()
        nums = 2
        x = s.generate2(nums)
        self.assertEqual(x, [[1],[1,1]])

    def test_generate_3(self):
        s = Solution()
        nums = 1
        x = s.generate(nums)
        self.assertEqual(x, [[1]])


