from unittest import TestCase
from isomorphic_strings import Solution


class TestSolution(TestCase):
    def test_is_isomorphic(self):
        s = Solution()
        s1, s2 = 'egg', 'add'
        x = s.isIsomorphic(s1, s2)
        self.assertTrue(x)

    def test_is_isomorphic2(self):
        s = Solution()
        s1, s2 = 'foo', 'bar'
        x = s.isIsomorphic(s1, s2)
        self.assertFalse(x)

    def test_is_isomorphic3(self):
        s = Solution()
        s1, s2 = 'paper', 'title'
        x = s.isIsomorphic(s1, s2)
        self.assertTrue(x)

    def test_is_isomorphic4(self):
        s = Solution()
        s1, s2 = 'badc', 'baba'
        x = s.isIsomorphic(s1, s2)
        self.assertFalse(x)
