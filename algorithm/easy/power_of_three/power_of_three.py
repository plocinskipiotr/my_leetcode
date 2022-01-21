class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n > 1:
            n, r = divmod(n, 3)
            if r:
                return False
        return True

    def isPowerOfThreeCarmack(self,n : int) -> bool:
        return n > 0 and 1162261467 % n == 0