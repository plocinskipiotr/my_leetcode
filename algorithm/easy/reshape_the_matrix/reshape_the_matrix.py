from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        size = len(mat) * len(mat[0])
        if size != r * c:
            return mat
        d1_array = [0] * size

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d1_array[i * len(mat[0]) + j] = mat[i][j]

        d2_array = [[0] * c for i in range(r)]

        for i in range(len(d1_array)):
            d2_array[i // c][i % c] = d1_array[i]

        print(d2_array)
