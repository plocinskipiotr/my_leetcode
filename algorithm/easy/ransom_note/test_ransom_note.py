from unittest import TestCase
from ransom_note import Solution


class TestSolution(TestCase):
    def test_can_construct(self):
        s = Solution()
        ransomNote, magazine = 'a', 'b'
        self.assertFalse(s.canConstruct(ransomNote, magazine))

    def test_can_construct1(self):
        s = Solution()
        ransomNote, magazine = 'aa', 'ab'
        self.assertFalse(s.canConstruct(ransomNote, magazine))

    def test_can_construct2(self):
        s = Solution()
        ransomNote, magazine = 'aa', 'aab'
        self.assertTrue(s.canConstruct(ransomNote, magazine))

