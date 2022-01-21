from unittest import TestCase
from find_the_difference import Solution


class TestSolution(TestCase):
    def test_find_the_difference(self):
        s = Solution()
        x = s.findTheDifference("abcd", "abcde")
        print(x)