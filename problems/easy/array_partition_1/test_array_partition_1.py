from unittest import TestCase
from array_partition_1 import Solution


class TestSolution(TestCase):
    def test_array_pair_sum(self):
        s = Solution()
        data = [4, 2, 3, 1]
        x = s.arrayPairSum(data)
        self.assertEqual(4, x)

    def test_array_pair_sum2(self):
        s = Solution()
        data = [6, 2, 6, 5, 1, 2]
        x = s.arrayPairSum(data)
        self.assertEqual(9, x)
