from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        new = list()
        last = [1, 1]
        j = 2
        for i in range(1, rowIndex):
            new.append(1)
            for i in range(1, j):
                new.append(last[i] + last[i - 1])
            j += 1
            new.append(1)
            last = new
            new = []

        return last
