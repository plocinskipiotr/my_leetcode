from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i = 0
        res = []
        lst = []
        while i < numRows:
            if i == 0:
                res = [1]
                lst.append(res)
            elif i == 1:
                res = [1, 1]
                lst.append(res)
            else:
                j = 0
                k = 1
                new: list[int] = list()
                new.append(1)
                while k < i:
                    new.append(res[j] + res[k])
                    j += 1
                    k += 1
                new.append(1)
                res = new
                lst.append(new)
            i += 1
        return lst

    def generate2(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        new = list()
        lists = [[1],[1,1]]
        j = 2
        for i in range(1, numRows - 1):
            last = lists[-1]
            new.append(1)
            for i in range(1, j):
                new.append(last[i] + last[i - 1])
            j += 1
            new.append(1)
            lists.append(new)
            new = []

        return lists