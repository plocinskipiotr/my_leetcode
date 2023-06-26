from unittest import TestCase
from counting_bits import Solution


class TestSolution(TestCase):
    def test_count_bits(self):
        s = Solution()
        data = 2
        d = s.countBits(data)
        self.assertEqual([0, 1, 1], d)

    def test_count_bits_2(self):
        s = Solution()
        data = 5
        d = s.countBitsDynamic(data)
        self.assertEqual([0, 1, 1, 2, 1, 2], d)

    def test_count_bits_3(self):
        s = Solution()
        data = 0
        d = s.countBits(data)
        self.assertEqual([0], d)

    def test_count_bits_4(self):
        s = Solution()
        data = 16
        d = s.countBitsDynamic(data)
        self.assertEqual([0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1], d)

    def test_count_bits_5(self):
        s = Solution()
        data = 2
        d = s.countBitsDynamic(data)
        self.assertEqual([0, 1, 1], d)
