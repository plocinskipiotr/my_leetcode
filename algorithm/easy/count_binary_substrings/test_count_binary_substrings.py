from unittest import TestCase
from count_binary_substrings import Solution


class TestSolution(TestCase):
    def test_count_binary_substrings(self):
        s = Solution()
        data = '10101'
        x = s.countBinarySubstrings(data)
        self.assertEqual(4, x)

    def test_count_binary_substrings2(self):
        s = Solution()
        data = '00110011'
        x = s.countBinarySubstrings(data)
        self.assertEqual(6, x)

    def test_count_binary_substrings3(self):
        s = Solution()
        data = '001001'
        x = s.countBinarySubstrings(data)
        self.assertEqual(3, x)

    def test_count_binary_substrings4(self):
        s = Solution()
        data = '1111111'
        x = s.countBinarySubstrings(data)
        self.assertEqual(0, x)
