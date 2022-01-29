from unittest import TestCase
from keyboard_row import Solution


class TestSolution(TestCase):
    def test_find_words(self):
        s = Solution()
        words = ["Hello", "Alaska", "Dad", "Peace"]
        x = s.findWords(words)
        self.assertEqual(["Alaska", "Dad"], x)
