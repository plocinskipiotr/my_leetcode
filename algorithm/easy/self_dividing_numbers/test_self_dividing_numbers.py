from unittest import TestCase
from self_dividing_numbers import Solution

class TestSolution(TestCase):
    def test_self_dividing_numbers(self):
        s = Solution()
        left,right = 1,22
        data = s.selfDividingNumbers(left,right)
        self.assertEqual([1,2,3,4,5,6,7,8,9,11,12,15,22],data)