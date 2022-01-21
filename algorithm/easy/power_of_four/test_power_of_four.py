from unittest import TestCase
from power_of_four import Solution

class TestSolution(TestCase):
    def test_is_power_of_four(self):
        s = Solution()
        data = 16
        self.assertTrue(s.isPowerOfFour(data))

    def test_is_power_of_four1(self):
        s = Solution()
        data = 17
        self.assertFalse(s.isPowerOfFour(data))

    def test_is_power_of_four2(self):
        s = Solution()
        data = 13
        self.assertFalse(s.isPowerOfFour(data))

    def test_is_power_of_four3(self):
        s = Solution()
        data = 32
        self.assertFalse(s.isPowerOfFour(data))

    def test_is_power_of_four4(self):
        s = Solution()
        data = 1
        self.assertFalse(s.isPowerOfFour(data))

    def test_is_power_of_four5(self):
        s = Solution()
        data = 2
        self.assertFalse(s.isPowerOfFour(data))

    def test_is_power_of_four6(self):
        s = Solution()
        data = 5
        self.assertFalse(s.isPowerOfFour(data))
