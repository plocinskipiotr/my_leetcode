from unittest import TestCase
from range_addition_2 import Solution


class TestSolution(TestCase):
    def test_max_count(self):
        s = Solution()
        x = s.maxCount(3, 3,
                       [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]])
        self.assertEqual(x, 4)
