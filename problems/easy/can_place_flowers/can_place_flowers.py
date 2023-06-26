from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return n == 0
            else:
                return n <= 1

        if flowerbed[:2] == [0, 0]:
            flowerbed[0] = 1
            n -= 1
        if flowerbed[-2:] == [0, 0]:
            flowerbed[-1] = 1
            n -= 1

        for i in range(1, len(flowerbed) - 2):
            if flowerbed[i - 1:i + 2] == [0, 0, 0]:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True

        if n <= 0:
            return True