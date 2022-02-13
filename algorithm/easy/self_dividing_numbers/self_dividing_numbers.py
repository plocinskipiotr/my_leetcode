from typing import List


class Solution:

    def check_divide(self, num: int):
        num_copy = num
        while num_copy:
            last_digit = num_copy % 10
            num_copy //= 10
            if last_digit == 0 or num % last_digit != 0:
                return None
        return num

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst = list()
        for num in range(left, right + 1):
            num = self.check_divide(num)
            if num:
                lst.append(num)
        return lst
