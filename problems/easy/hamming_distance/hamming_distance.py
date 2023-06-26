class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ones = x ^ y

        ones_sum = 0
        while ones:
            if ones & 1:
                ones_sum += 1
            ones >>= 1
        return ones_sum
