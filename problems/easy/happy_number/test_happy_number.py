from unittest import TestCase
from happy_number import Solution


class TestSolution(TestCase):
    def test_is_happy(self):
        s = Solution()
        n = 19
        x = s.isHappyTurtle(n)
        self.assertTrue(x)

    def test_is_happy2(self):
        s = Solution()
        n = 7
        x = s.isHappyTurtle(n)
        self.assertTrue(x)

    def test_is_happy3(self):
        s = Solution()
        n = 116
        x = s.isHappyTurtle(n)
        self.assertFalse(x)
