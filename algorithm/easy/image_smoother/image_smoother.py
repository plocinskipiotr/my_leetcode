from typing import List


class Solution:
    def isIndexValid(self, x, y, img):
        if x >= 0 and x < len(img) and y >= 0 and y < len(img[0]):
            return True
        else:
            return False

    def calc_mean(self, x, y, img):
        suma = 0
        cnt = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.isIndexValid(x - i, y - j, img):
                    suma += img[x - i][y - j]
                    cnt += 1

        return suma // cnt

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        new_img = [[0] * len(img[0]) for i in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[0])):
                new_img[i][j] = self.calc_mean(i, j, img)

        return new_img
