from unittest import TestCase
from pascal_triangle import Solution


class TestSolution(TestCase):
    def test_get_row(self):
        s = Solution()
        x = s.getRow(4)
        self.assertEqual([1, 3, 3, 1], x)
