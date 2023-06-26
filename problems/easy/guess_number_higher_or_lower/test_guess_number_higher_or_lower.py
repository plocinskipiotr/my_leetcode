from unittest import TestCase
from guess_number_higher_or_lower import Solution

class TestSolution(TestCase):
    def test_guess_number(self):
        s = Solution()
        self.assertEqual(6,s.guessNumber(10))
