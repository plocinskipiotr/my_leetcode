from unittest import TestCase
from reverse_string import Solution


class TestSolution(TestCase):
    def test_reverse_str(self):
        s = Solution()
        x = s.reverseStr('abcd', 2)
        print(x)

    def test_reverse_str2(self):
        s = Solution()
        x = s.reverseStr('abcdefgh', 2)
        print(x)

    def test_reverse_str3(self):
        s = Solution()
        x = s.reverseStr('abcdef', 4)
        print(x)

