from unittest import TestCase
from add_strings import Solution


class TestSolution(TestCase):
    def test_add_strings(self):
        s = Solution()
        x = s.addStrings("12", "12")
        self.assertEqual("24", x)

    def test_add_strings2(self):
        s = Solution()
        x = s.addStrings("49", "12")
        self.assertEqual("61", x)

    def test_add_strings3(self):
        s = Solution()
        x = s.addStrings("999", "12")
        self.assertEqual("1011", x)