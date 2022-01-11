from unittest import TestCase
from add_binary import Solution


class TestSolution(TestCase):
    def test_add_binary_1(self):
        s = Solution()
        a = '1'
        b = '1'
        r = s.addBinary(a, b)
        self.assertEqual('10', r)

    def test_add_binary_2(self):
        s = Solution()
        a = '0'
        b = '0'
        r = s.addBinary(a, b)
        self.assertEqual('0', r)

    def test_add_binary_3(self):
        s = Solution()
        a = '0'
        b = '1'
        r = s.addBinary(a, b)
        self.assertEqual('1', r)

    def test_add_binary_4(self):
        s = Solution()
        a = '11'
        b = '1'
        r = s.addBinary(a, b)
        self.assertEqual('100', r)

    def test_add_binary_5(self):
        s = Solution()
        a = '1010'
        b = '1011'
        r = s.addBinary(a, b)
        self.assertEqual('10101', r)

    def test_add_binary_6(self):
        s = Solution()
        a = '11'
        b = '1'
        r = s.addBinary(a, b)
        self.assertEqual('100', r)

