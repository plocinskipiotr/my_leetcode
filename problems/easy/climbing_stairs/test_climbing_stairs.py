from unittest import TestCase
from climbing_stairs import Solution


class TestSolution(TestCase):
    def test_climb_stairs1(self):
        s = Solution()
        n = 1
        a = s.climbStairs(n)
        self.assertEqual(1, a)

    def test_climb_stairs2(self):
        s = Solution()
        n = 2
        a = s.climbStairs(n)
        self.assertEqual(2, a)

    def test_climb_stairs3(self):
        s = Solution()
        n = 3
        a = s.climbStairs(n)
        self.assertEqual(3, a)

    def test_climb_stairs4(self):
        s = Solution()
        n = 4
        a = s.climbStairs(n)
        self.assertEqual(5, a)

    def test_climb_stairs5(self):
        s = Solution()
        n = 5
        a = s.climbStairs(n)
        self.assertEqual(8, a)
