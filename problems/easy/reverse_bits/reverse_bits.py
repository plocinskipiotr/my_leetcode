class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        size = 32
        for i in range(size):
            bit = (n >> i) & 1
            res = res | (bit << size - 1 - i)
        return res
