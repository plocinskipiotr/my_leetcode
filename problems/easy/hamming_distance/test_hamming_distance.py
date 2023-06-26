from unittest import TestCase
from hamming_distance import Solution


class TestSolution(TestCase):
    def test_hamming_distance(self):
        s = Solution()
        a, b = 1, 3
        c = s.hammingDistance(a, b)
        self.assertEqual(1, c)

    def test_hamming_distance2(self):
        s = Solution()
        a, b = 2, 2
        c = s.hammingDistance(a, b)
        self.assertEqual(0, c)