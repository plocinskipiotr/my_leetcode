from unittest import TestCase
from power_of_three import Solution

class TestSolution(TestCase):
    def test_is_power_of_three(self):
        s = Solution()
        d = 27
        self.assertTrue(s.isPowerOfThree(d))
        d = 4
        self.assertFalse(s.isPowerOfThree(d))