from unittest import TestCase
from longest_palindrome import Solution


class TestSolution(TestCase):
    def test_longest_palindrome(self):
        s = Solution()
        data = 'abccccdd'
        x = s.longestPalindrome(data)
        self.assertEqual(x, 7)

    def test_longest_palindrome2(self):
        s = Solution()
        data = 'a'
        x = s.longestPalindrome(data)
        self.assertEqual(x, 1)

    def test_longest_palindrome3(self):
        s = Solution()
        data = 'abcdee'
        x = s.longestPalindrome(data)
        self.assertEqual(x, 3)

    def test_longest_palindrome4(self):
        s = Solution()
        data = 'abab'
        x = s.longestPalindrome(data)
        self.assertEqual(x, 4)

