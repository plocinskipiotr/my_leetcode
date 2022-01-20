from unittest import TestCase
from move_zeroes import Solution


class TestSolution(TestCase):
    def test_move_zeroes(self):
        s = Solution()
        data = [0, 1, 0, 3, 12]
        x = s.moveZeroes(data)
        self.assertEqual([1, 3, 12, 0, 0], data)

    def test_move_zeroes1(self):
        s = Solution()
        data = [0]
        x = s.moveZeroes(data)
        self.assertEqual([0], data)

    def test_move_zeroes2(self):
        s = Solution()
        data = [1, 2, 0, 3, 6, 7, 0]
        s.moveZeroes(data)
        self.assertEqual([1, 2, 3, 6, 7, 0, 0], data)
