from unittest import TestCase
from construct_the_rectangle import Solution


class TestSolution(TestCase):
    def test_construct_rectangle(self):
        s = Solution()
        area = 234
        x = s.constructRectangle(area)
        self.assertEqual([18, 13], x)

    def test_construct_rectangle2(self):
        s = Solution()
        area = 170
        x = s.constructRectangle(area)
        self.assertEqual([17, 10], x)
