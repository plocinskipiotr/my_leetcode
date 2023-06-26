from unittest import TestCase
from binary_watch import Solution

class TestSolution(TestCase):
    def test_readBinaryWatch(self):
        s = Solution()
        x = s.readBinaryWatch_2(9)
