from unittest import TestCase
from is_subsequence import Solution


class TestSolution(TestCase):
    def test_is_subsequence(self):
        s = Solution()
        s1, s2 = 'abc', 'ahbgdc'

        self.assertTrue(s.isSubsequence(s1, s2))

    def test_is_subsequence2(self):
        s = Solution()
        s1, s2 = 'axc', 'ahbgdc'

        self.assertFalse(s.isSubsequence(s1, s2))

    def test_is_subsequence3(self):
        s = Solution()
        s1, s2 = 'aaaaaa', 'bbaaaa'

        self.assertFalse(s.isSubsequence(s1, s2))

    def test_is_subsequence4(self):
        s = Solution()
        s1, s2 = 'abc', 'acb'

        self.assertFalse(s.isSubsequence(s1, s2))

    def test_is_subsequence5(self):
        s = Solution()
        s1, s2 = 'ab', 'baab'

        self.assertTrue(s.isSubsequence(s1, s2))

