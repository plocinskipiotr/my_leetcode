from unittest import TestCase
from reverse_vowels_of_a_string import Solution


class TestSolution(TestCase):
    def test_reverse_vowels(self):
        s = Solution()
        data = 'hello'
        s1 = s.reverseVowels(data)
        self.assertEqual('holle', s1)

    def test_reverse_vowels2(self):
        s = Solution()
        data = 'leetcode'
        s1 = s.reverseVowels(data)
        self.assertEqual('leotcede', s1)

    def test_reverse_vowels3(self):
        s = Solution()
        data = "Euston saw I was not Sue."
        s1 = s.reverseVowels(data)
        self.assertEqual("euston saw I was not SuE.", s1)


