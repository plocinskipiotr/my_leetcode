class Solution:
    def toHex(self, num: int) -> str:
        s = ''
        hex = '0123456789abcdef'

        if num < 0:
            num += 2 << 31

        while num:
            s = hex[num & 15] + s
            num >>= 4

        return s if len(s) > 0 else '0'
