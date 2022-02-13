from unittest import TestCase
from find_pivot_index import Solution


class TestSolution(TestCase):
    def test_pivot_index(self):
        s = Solution()
        data = [1, 7, 3, 6, 5, 6]
        x = s.pivotIndex(data)
        self.assertEqual(x, 3)

    def test_pivot_index2(self):
        s = Solution()
        data = [-1,-1,-1,-1,0,1]
        x = s.pivotIndex(data)
        self.assertEqual(x, 1)

    def test_pivot_index3(self):
        s = Solution()
        data = [2,1,-1]
        x = s.pivotIndex(data)
        self.assertEqual(x, 0)
