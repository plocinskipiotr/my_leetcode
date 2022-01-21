from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        lst = list()
        for i in range(n + 1):
            ones = 0
            while i > 0:
                bit = i & 1
                i >>= 1
                ones += bit
            lst.append(ones)
        return lst

    def countBitsDynamic(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        lst = [0, 1, 1]
        check_point, next_check_point = 2, 4

        for j in range(3, n + 1):

            if j == check_point * 2:
                check_point = j

            new_num = 1 + lst[j - check_point]
            lst.append(new_num)

        return lst
