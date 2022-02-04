from unittest import TestCase
from binary_number_with_alternating_bits import Solution


class TestSolution(TestCase):
    def test_has_alternating_bits(self):
        s = Solution()
        x = s.hasAlternatingBits(5)
        self.assertTrue(x)

    def test_has_alternating_bits2(self):
        s = Solution()
        x = s.hasAlternatingBits(6)
        self.assertFalse(x)

    def test_has_alternating_bits3(self):
        s = Solution()
        x = s.hasAlternatingBits(1)
        self.assertTrue(x)

    def test_has_alternating_bits4(self):
        s = Solution()
        x = s.hasAlternatingBits(2)
        self.assertTrue(x)

    def test_has_alternating_bits5(self):
        s = Solution()
        x = s.hasAlternatingBits(3)
        self.assertFalse(x)

