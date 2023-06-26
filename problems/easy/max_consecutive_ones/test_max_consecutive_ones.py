from unittest import TestCase
from max_consecutive_ones import Solution


class TestSolution(TestCase):
    def test_find_max_consecutive_ones(self):
        s = Solution()
        nums = [1, 1, 0, 1, 1, 1]
        x = s.findMaxConsecutiveOnes(nums)
        self.assertEqual(3, x)

    def test_find_max_consecutive_ones2(self):
        s = Solution()
        nums = [1, 0, 1, 1, 0, 1]
        x = s.findMaxConsecutiveOnes(nums)
        self.assertEqual(2, x)
