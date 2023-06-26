from unittest import TestCase
from valid_anagram import Solution

class TestSolution(TestCase):
    def test_is_anagram(self):
        s = Solution()
        s1 = "anagram"
        s2 = "nagaram"
        x = s.isAngramsort(s1,s2)
        self.assertTrue(x)