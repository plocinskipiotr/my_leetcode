from unittest import TestCase
from reverse_string import Solution


class TestSolution(TestCase):
    def test_reverse_string(self):
        s = Solution()
        s1 = ["h", "e", "l", "l", "o"]
        s.reverseString(s1)
        self.assertEqual(["o", "l", "l", "e", "h"], s1)
