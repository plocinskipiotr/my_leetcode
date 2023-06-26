class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        last_bit = n & 1
        n >>= 1
        while n:
            new_last_bit = n & 1

            if new_last_bit ^ last_bit == 0:
                return False

            last_bit = new_last_bit
            n >>= 1
        return True
