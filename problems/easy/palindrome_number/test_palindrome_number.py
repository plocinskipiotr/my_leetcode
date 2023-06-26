from unittest import TestCase

from palindrome_number import Solution


class TestSolution(TestCase):
    def test_is_palindrome(self):
        s = Solution()
        data = 0
        x = s.isPalindrome(data)
        self.assertEqual(x, True)

        data = 1
        x = s.isPalindrome(data)
        self.assertEqual(x, True)

        data = -1
        x = s.isPalindrome(data)
        self.assertEqual(x, False)

        data = 10
        x = s.isPalindrome(data)
        self.assertEqual(x, False)

        data = -10
        x = s.isPalindrome(data)
        self.assertEqual(x, False)

        data = 101
        x = s.isPalindrome(data)
        self.assertEqual(x, True)

        data = 400004
        x = s.isPalindrome(data)
        self.assertEqual(x, True)

        data = 12321
        x = s.isPalindrome(data)
        self.assertEqual(x, True)

    def test_is_palindrome_numerical(self):
        s = Solution()
        data = 1000
        y = s.is_palindrome_numerical(data)
        self.assertFalse(y)

        data = 1
        y = s.is_palindrome_numerical(data)
        self.assertTrue(y)

        data = 12345
        y = s.is_palindrome_numerical(data)
        self.assertFalse(y)

        data = 1001
        y = s.is_palindrome_numerical(data)
        self.assertTrue(y)
