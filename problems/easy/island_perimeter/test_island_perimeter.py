from unittest import TestCase
from island_perimeter import Solution, Solution2


class TestSolution(TestCase):
    def test_island_perimeter(self):
        s = Solution2()
        grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        x = s.islandPerimeterBFS(grid)
        self.assertEqual(x, 16)

    def test_island_perimeter2(self):
        s = Solution2()
        grid = [[1, 0]]
        x = s.islandPerimeterBFS(grid)
        self.assertEqual(x, 4)

    def test_island_perimeter3(self):
        s = Solution2()
        grid = [[1, 1]]
        x = s.islandPerimeterBFS(grid)
        self.assertEqual(x, 6)

    def test_island_perimeter4(self):
        s = Solution2()
        grid = [[0], [1]]
        x = s.islandPerimeterBFS(grid)
        self.assertEqual(x, 4)

    def test_island_perimeter5(self):
        s = Solution2()
        grid = [[1, 1], [1, 1]]
        x = s.islandPerimeterBFS(grid)
        self.assertEqual(x, 8)

    def test_island_perimeter6(self):
        s = Solution2()
        grid = [[1, 1, 0], [1, 1, 1]]
        x = s.islandPerimeterBFS(grid)
        self.assertEqual(x, 8)

    def test_island_perimeterDFS(self):
        s = Solution2()
        grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        x = s.islandPerimeterDFS(grid)
        self.assertEqual(x, 16)

    def test_island_perimeterDFS2(self):
        s = Solution2()
        grid = [[1, 0]]
        x = s.islandPerimeterDFS(grid)
        self.assertEqual(x, 4)

    def test_island_perimeterDFS3(self):
        s = Solution2()
        grid = [[1, 1]]
        x = s.islandPerimeterDFS(grid)
        self.assertEqual(x, 6)

    def test_island_perimeterDFS4(self):
        s = Solution2()
        grid = [[0], [1]]
        x = s.islandPerimeterDFS(grid)
        self.assertEqual(x, 4)

    def test_island_perimeterDFS5(self):
        s = Solution2()
        grid = [[1, 1], [1, 1]]
        x = s.islandPerimeterDFS(grid)
        self.assertEqual(x, 8)

    def test_island_perimeterDFS6(self):
        s = Solution2()
        grid = [[1, 1, 0], [1, 1, 1]]
        x = s.islandPerimeterDFS(grid)
        self.assertEqual(x, 8)
