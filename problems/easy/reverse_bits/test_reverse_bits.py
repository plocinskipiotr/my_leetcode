from unittest import TestCase
from reverse_bits import Solution


class TestSolution(TestCase):
    def test_reverse_bits(self):
        data = 43261596
        s = Solution()
        d = s.reverseBits(data)
        self.assertEqual(964176192, d)
