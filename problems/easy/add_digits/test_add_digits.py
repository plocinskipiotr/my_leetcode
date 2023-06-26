from unittest import TestCase
from add_digits import Solution


class TestSolution(TestCase):
    def test_add_digits0(self):
        nums = 38
        s =Solution()
        p = s.addDigits(nums)
        self.assertEqual(2, p)

    def test_add_digits1(self):
        nums = 0
        s =Solution()
        p = s.addDigits(nums)
        self.assertEqual(0, p)

    def test_add_digits3(self):
        nums = 99
        s =Solution()
        p = s.addDigits(nums)
        self.assertEqual(9, p)

