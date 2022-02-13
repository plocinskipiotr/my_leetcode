from unittest import TestCase
from find_smallest_letter_greater_than_target import Solution


class TestSolution(TestCase):
    def test_next_greatest_letter(self):
        s = Solution()
        letters = ["c", "f", "j"]
        target = 'd'
        x = s.nextGreatestLetter(letters, target)
        self.assertEqual('f', x)

    def test_next_greatest_letter2(self):
        s = Solution()
        letters = ["c", "f", "j"]
        target = 'g'
        x = s.nextGreatestLetter(letters, target)
        self.assertEqual('j', x)

    def test_next_greatest_letter3(self):
        s = Solution()
        letters = ["e","e","e","e","e","e","n","n","n","n"]
        target = "e"
        x = s.nextGreatestLetter(letters, target)
        self.assertEqual('n', x)




