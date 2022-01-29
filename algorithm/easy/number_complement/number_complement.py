class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        i = 0
        while num:
            char = (int(not (num & 1)))
            char <<= i
            num >>= 1
            i += 1
            res += char
        return res

    def findComplementXOR(self, num: int) -> int:
        mask = 1

        while mask < num:
            mask <<= 1
            mask |= 1

        return mask ^ num
