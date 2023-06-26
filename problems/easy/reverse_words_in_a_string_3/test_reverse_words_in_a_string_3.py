from unittest import TestCase
from reverse_words_in_a_string_3 import Solution

class TestSolution(TestCase):
    def test_reverse_words(self):
        s = Solution()
        s1 = "Let's take LeetCode contest"
        x = s.reverseWords(s1)
        self.assertEqual("s'teL ekat edoCteeL tsetnoc",x)
