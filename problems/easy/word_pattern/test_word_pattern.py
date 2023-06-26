from unittest import TestCase
from word_pattern import Solution


class TestSolution(TestCase):
    def test_word_pattern(self):
        s = Solution()
        s1 = 'dog cat cat dog'
        p = 'abba'
        self.assertTrue(s.wordPattern(p, s1))
        s1 = 'dog cat cat fish'
        p = 'abba'
        self.assertFalse(s.wordPattern(p, s1))
        s1 = 'dog dog dog dog'
        p = 'abba'
        self.assertFalse(s.wordPattern(p, s1))
        s1 = 'jquery'
        p = 'jquery'
        self.assertFalse(s.wordPattern(p, s1))
