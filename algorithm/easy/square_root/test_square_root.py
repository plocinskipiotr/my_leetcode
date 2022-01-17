from unittest import TestCase

from square_root import Solution

class TestSolution(TestCase):
    def test_my_sqrt_00(self):
        s = Solution()
        x = 0
        r = s.mySqrt(x)
        self.assertEqual(0,r)

    def test_my_sqrt_0(self):
        s = Solution()
        x = 1
        r = s.mySqrt(x)
        self.assertEqual(1,r)

    def test_my_sqrt(self):
        s = Solution()
        x = 4
        r = s.mySqrt(x)
        self.assertEqual(2,r)

    def test_my_sqrt_1(self):
        s = Solution()
        x = 8
        r = s.mySqrt(x)
        self.assertEqual(2,r)

    def test_my_sqrt_3(self):
        s = Solution()
        x = 10
        r = s.mySqrt(x)
        self.assertEqual(3,r)

    def test_my_sqrt_2(self):
        s = Solution()
        x = 12
        r = s.mySqrt(x)
        self.assertEqual(3,r)

