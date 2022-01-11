from unittest import TestCase

from length_of_last_word import Solution


class TestSolution(TestCase):
    def test_length_of_last_word_0(self):
        s = Solution()
        input = 'Hello World'
        d = s.lengthOfLastWord(input)
        self.assertEqual(d, 5)

    def test_length_of_last_word_1(self):
        s = Solution()
        input = "   fly me   to   the moon  "
        d = s.lengthOfLastWord(input)
        self.assertEqual(d, 4)

    def test_length_of_last_word_2(self):
        s = Solution()
        input = "luffy is still joyboy"
        d = s.lengthOfLastWord(input)
        self.assertEqual(d, 6)

    def test_length_of_last_word_3(self):
        s = Solution()
        input = "x"
        d = s.lengthOfLastWord(input)
        self.assertEqual(d, 1)

    def test_length_of_last_word_4(self):
        s = Solution()
        input = " x"
        d = s.lengthOfLastWord(input)
        self.assertEqual(d, 1)

    def test_length_of_last_word_5(self):
        s = Solution()
        input = "x "
        d = s.lengthOfLastWord(input)
        self.assertEqual(d, 1)