from typing import List
from collections import deque


class Solution:
    def is_valid(self, grid, row, col):
        return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])

    def neigbours(self, grid, row, col):
        suma = 0
        indices = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for row, col in indices:
            if self.is_valid(grid, row, col) and grid[row][col] == 1:
                pass
            else:
                suma += 1
        return suma

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        suma = row = col = 0
        while row < len(grid):
            while col < len(grid[row]):
                if grid[row][col] == 1:
                    suma += self.neigbours(grid, row, col)
                col += 1
            col = 0
            row += 1
        return suma


class Solution2:
    sum_hashmap = {4: 0, 3: 1, 2: 2, 1: 3, 0: 4}

    def is_index_valid(self, grid, row, col):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row])

    def neighbours(self, grid, row, col, ref):
        indices = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        valid_neighbours = list()
        for row, col in indices:
            if self.is_index_valid(grid, row, col) and grid[row][col] == grid[ref[0]][ref[1]]:
                valid_neighbours.append((row, col))
        return valid_neighbours

    def findStart(self, grid: List[List[int]]) -> tuple[int, int]:
        reference = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    reference = (row, col)
                    break
            if reference:
                break
        return reference

    def islandPerimeterBFS(self, grid: List[List[int]]) -> int:
        suma = 0
        reference = self.findStart(grid)
        que = deque([reference])
        visited = set()
        while que:
            row, col = que.popleft()
            if (row, col) not in visited:
                visited.add((row, col))
                neighbours = self.neighbours(grid, row, col, reference)
                suma += self.sum_hashmap[len(neighbours)]
                for neighbour in neighbours:
                    que.append(neighbour)
        return suma

    def islandPerimeterDFS(self, grid: List[List[int]]) -> int:
        suma = 0
        reference = self.findStart(grid)
        que = deque([reference])
        visited = set()
        while que:
            row, col = que.pop()
            if (row, col) not in visited:
                visited.add((row, col))
                neighbours = self.neighbours(grid, row, col, reference)
                suma += self.sum_hashmap[len(neighbours)]
                for neighbour in neighbours:
                    que.append(neighbour)
        return suma
