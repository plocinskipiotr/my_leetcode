class Solution:
    def hammingWeight(self, n: int) -> int:
        size = 32
        ones = 0
        for i in range(size):
            if (n >> i) & 1:
                ones += 1
        return ones
