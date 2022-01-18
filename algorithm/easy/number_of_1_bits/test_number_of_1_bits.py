from unittest import TestCase
from number_of_1_bits import Solution


class TestSolution(TestCase):
    def test_hamming_weight(self):
        s = Solution()
        data = 7
        x = s.hammingWeight(data)
        self.assertEqual(3, x)
