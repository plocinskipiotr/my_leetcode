from itertools import combinations
from typing import List


def filterfunc(x):
    suma = sum(x)
    if suma >= 768:
        return False

    suma = 0
    for i in x:
        if i < 64:
            suma += i

    if suma >= 60:
        return False
    return True


def translate_hour(x):
    if x == 512:
        return 8
    elif x == 256:
        return 4
    elif x == 128:
        return 2
    else:
        return 1


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []

        x = combinations([512, 256, 128, 64, 32, 16, 8, 4, 2, 1], turnedOn)
        x = list(filter(filterfunc, x))
        res = list()
        for el in x:
            H = 0
            M = 0
            for tup in el:
                if tup < 64:
                    M += tup
                else:
                    H += translate_hour(tup)
            res.append(str(H) + ':' + f'{M:02d}')
        return res


    def readBinaryWatch_2(self,turnedOn: int) -> List[str]:
        lst = list()
        for i in range(12):
            for j in range(60):
                if (bin(i) + bin(j)).count('1') == turnedOn:
                    lst.append(str(i) + ':' + str(j).zfill(2))
        return lst