from unittest import TestCase
from ugly_number import Solution

class TestSolution(TestCase):
    def test_is_ugly(self):
        s = Solution()
        x = 32

        self.assertTrue(s.isUgly(x))

        x = 31
        self.assertFalse(s.isUgly(x))