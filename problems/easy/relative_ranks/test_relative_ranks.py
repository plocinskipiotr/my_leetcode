from unittest import TestCase
from relative_ranks import Solution


class TestSolution(TestCase):
    def test_find_relative_ranks(self):
        s = Solution()
        data = [10, 3, 8, 9, 4]
        x = s.findRelativeRanks(data)
        self.assertEqual(['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4'], x)
