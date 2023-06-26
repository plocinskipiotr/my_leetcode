from unittest import TestCase
from reshape_the_matrix import Solution


class TestSolution(TestCase):
    def test_matrix_reshape(self):
        s = Solution()
        data = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        s.matrixReshape(data, 3, 3)

    def test_matrix_reshape2(self):
        s = Solution()
        data = [[0, 1], [2, 3], [4, 5]]
        s.matrixReshape(data, 3, 2)

    def test_matrix_reshape3(self):
        s = Solution()
        data = [[0], [1], [2]]
        s.matrixReshape(data, 3, 1)

    def test_matrix_reshape4(self):
        s = Solution()
        data = [[0,1], [2,3]]
        s.matrixReshape(data, 1, 4)