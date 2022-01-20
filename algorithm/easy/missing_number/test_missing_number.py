from unittest import TestCase
from missing_number import Solution

class TestSolution(TestCase):
    def test_missing_number(self):
        s = Solution()
        nums = [3,0,1]
        x = s.missingNumber(nums)
        self.assertEqual(2,x)

    def test_missing_number1(self):
        s = Solution()
        nums = [0,1]
        x = s.missingNumber(nums)
        self.assertEqual(2,x)

    def test_missing_number2(self):
        s = Solution()
        nums = [9,6,4,2,3,5,7,0,1]
        x = s.missingNumber(nums)
        self.assertEqual(8,x)

    def test_missing_number3(self):
        s = Solution()
        nums = [0]
        x = s.missingNumber(nums)
        self.assertEqual(1,x)

