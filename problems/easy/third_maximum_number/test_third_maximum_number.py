from unittest import TestCase
from third_maximum_number import Solution


class TestSolution(TestCase):
    def test_third_max(self):
        s = Solution()
        nums = [3, 2, 1]
        x = s.thirdMaxSet(nums)
        self.assertEqual(1, x)

    def test_third_max1(self):
        s = Solution()
        nums = [1,2]
        x = s.thirdMaxSet(nums)
        self.assertEqual(2, x)

    def test_third_max2(self):
        s = Solution()
        nums = [2,2,3,1]
        x = s.thirdMaxSet(nums)
        self.assertEqual(1, x)
