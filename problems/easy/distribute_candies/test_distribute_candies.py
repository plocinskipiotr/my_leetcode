from unittest import TestCase
from distribute_candies import Solution


class TestSolution(TestCase):
    def test_distribute_candies(self):
        s = Solution()
        x = s.distributeCandies([1, 1, 2, 2, 3, 3])
        self.assertEqual(x, 3)

    def test_distribute_candies2(self):
        s = Solution()
        x = s.distributeCandies([1, 1, 2, 3])
        self.assertEqual(x, 2)

    def test_distribute_candies3(self):
        s = Solution()
        x = s.distributeCandies([6, 6, 6, 6])
        self.assertEqual(x, 1)
