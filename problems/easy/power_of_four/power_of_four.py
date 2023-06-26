import math


class Solution:
    def isPowerOfFourMath(self, n: int) -> bool:
        if n <= 0:
            return False

        return (math.log(n) / math.log(4)).is_integer()

    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        while n:
            n, r = divmod(n, 4)
            if r:
                return False
            if n == 1:
                return True

    def isPowerOfFourReccursive(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 4:
            return False

        return self.isPowerOfFourReccursive(n // 4)
