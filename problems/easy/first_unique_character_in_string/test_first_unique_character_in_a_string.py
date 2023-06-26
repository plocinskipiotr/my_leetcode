from unittest import TestCase
from first_unique_character_in_a_string import Solution


class TestSolution(TestCase):
    def test_first_uniq_char(self):
        s = Solution()
        x = s.firstUniqChar("leetcode")
        self.assertEqual(0, x)

    def test_first_uniq_char1(self):
        s = Solution()
        x = s.firstUniqChar("loveleetcode")
        self.assertEqual(2, x)
