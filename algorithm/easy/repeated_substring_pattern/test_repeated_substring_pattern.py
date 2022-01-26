from unittest import TestCase
from repeated_substring_pattern import Solution


class TestSolution(TestCase):
    def test_repeated_substring_pattern(self):
        s = Solution()
        s1 = 'abab'
        x = s.repeatedSubstringPattern2(s1)
        self.assertTrue(x)

    def test_repeated_substring_pattern2(self):
        s = Solution()
        s1 = 'abcabcabcabc'
        x = s.repeatedSubstringPattern2(s1)
        self.assertTrue(x)

    def test_repeated_substring_pattern3(self):
        s = Solution()
        s1 = 'abcdefgabcdefgabcdefgabcdefg'
        x = s.repeatedSubstringPattern2(s1)
        self.assertTrue(x)

    def test_repeated_substring_pattern4(self):
        s = Solution()
        s1 = 'aaaaaaaaaaaa'
        x = s.repeatedSubstringPattern2(s1)
        self.assertTrue(x)

    def test_repeated_substring_pattern5(self):
        s = Solution()
        s1 = 'ababba'
        x = s.repeatedSubstringPattern2(s1)
        self.assertFalse(x)

    def test_repeated_substring_pattern6(self):
        s = Solution()
        s1 = 'aabaaba'
        x = s.repeatedSubstringPattern2(s1)
        self.assertFalse(x)
