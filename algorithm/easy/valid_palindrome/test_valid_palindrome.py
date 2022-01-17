from unittest import TestCase
from valid_palindrome import Solution

class TestSolution(TestCase):
    def test_is_palindrome(self):
        s = Solution()
        data: str = "A man, a plan, a canal: Panama"
        r = s.isPalindrome(data)
        self.assertTrue(r)

    def test_is_palindrome1(self):
        s = Solution()
        data: str = "race a car"
        r = s.isPalindrome(data)
        self.assertFalse(r)

    def test_is_palindrome2(self):
        s = Solution()
        data: str = " "
        r = s.isPalindrome(data)
        self.assertTrue(r)

    def test_is_palindrome3(self):
        s = Solution()
        data: str = "aa"
        r = s.isPalindrome(data)
        self.assertTrue(r)

    def test_is_palindrome4(self):
        s = Solution()
        data: str = "0P"
        r = s.isPalindrome(data)
        self.assertFalse(r)