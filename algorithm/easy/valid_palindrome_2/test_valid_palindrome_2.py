from unittest import TestCase
from valid_palindrome_2 import Solution


class TestSolution(TestCase):
    def test_valid_palindrome(self):
        s = Solution()
        data = 'aba'
        x = s.validPalindrome(data)
        self.assertTrue(x)

    def test_valid_palindrome3(self):
        s = Solution()
        data = 'abc'
        x = s.validPalindrome(data)
        self.assertFalse(x)

    def test_valid_palindrome2(self):
        s = Solution()
        data = 'abca'
        x = s.validPalindrome(data)
        self.assertTrue(x)

    def test_valid_palindrome4(self):
        s = Solution()
        data = 'abcda'
        x = s.validPalindrome(data)
        self.assertFalse(x)
