from typing import List
from collections import deque


class Solution:

    def is_index_valid(self, imageList: [List[int]], y: int, x: int):
        if x >= 0 and x < len(imageList[0]) and y >= 0 and y < len(imageList):
            return True
        return False

    def traverse_graph(self, image: List[List[int]], y: int, x: int, oldColor: int, newColor: int):

        if self.is_index_valid(image, y, x):
            if image[y][x] == oldColor:
                image[y][x] = newColor

                self.traverse_graph(image, y + 1, x, oldColor, newColor)
                self.traverse_graph(image, y - 1, x, oldColor, newColor)
                self.traverse_graph(image, y, x + 1, oldColor, newColor)
                self.traverse_graph(image, y, x - 1, oldColor, newColor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor: return image
        self.traverse_graph(image, sr, sc, oldColor, newColor)
        return image

    def floodFillIter(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor: return image
        deq = deque()
        deq.append((sr, sc))

        while len(deq):
            y, x = deq.pop()
            if self.is_index_valid(image, y, x):
                if image[y][x] == oldColor:
                    image[y][x] = newColor
                    deq.append((y + 1, x))
                    deq.append((y - 1, x))
                    deq.append((y, x + 1))
                    deq.append((y, x - 1))
        return image