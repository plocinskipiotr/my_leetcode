from unittest import TestCase
from flood_fill import Solution


class TestSolution(TestCase):
    def test_flood_fill(self):
        s = Solution()
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        newColor = 2
        s.floodFill(image, sr, sc, newColor)
        self.assertEqual([[2, 2, 2], [2, 2, 0], [2, 0, 1]], image)

    def test_flood_fill2(self):
        s = Solution()
        image = [[0,0,0],[0,0,0]]
        sr = 0
        sc = 0
        newColor = 2
        s.floodFill(image, sr, sc, newColor)
        self.assertEqual([[2,2,2],[2,2,2]], image)

    def test_flood_fill3(self):
        s = Solution()
        image = [[0,0,0],[0,1,1]]
        sr = 1
        sc = 1
        newColor = 1
        s.floodFill(image, sr, sc, newColor)
        self.assertEqual([[2,2,2],[2,2,2]], image)


    def test_flood_fill_iter(self):
        s = Solution()
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        newColor = 2
        s.floodFillIter(image, sr, sc, newColor)
        self.assertEqual([[2, 2, 2], [2, 2, 0], [2, 0, 1]], image)
