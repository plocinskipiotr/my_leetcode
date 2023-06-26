from unittest import TestCase
from baseball_game import Solution


class TestSolution(TestCase):
    def test_cal_points(self):
        s = Solution()
        ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
        suma = s.calPoints(ops)
        self.assertEqual(suma, 27)

    def test_cal_points2(self):
        s = Solution()
        ops = ["5","2","C","D","+"]
        suma = s.calPoints(ops)
        self.assertEqual(suma, 30)
    def test_cal_points3(self):
        s = Solution()
        ops = ["1"]
        suma = s.calPoints(ops)
        self.assertEqual(suma, 1)
