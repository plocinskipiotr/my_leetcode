from unittest import TestCase
from assign_cookies import Solution


class TestSolution(TestCase):
    def test_find_content_children(self):
        s = Solution()
        g = [1, 2, 3]
        s1 = [1, 1]
        x = s.findContentChildren(g, s1)
        self.assertEqual(1, x)

    def test_find_content_children2(self):
        s = Solution()
        g = [1, 2]
        s1 = [1, 2, 3]
        x = s.findContentChildren(g, s1)
        self.assertEqual(2, x)

    def test_find_content_children3(self):
        s = Solution()
        g = [10, 9, 8, 7]
        s1 = [5, 6, 7, 8]
        x = s.findContentChildren(g, s1)
        self.assertEqual(2, x)
