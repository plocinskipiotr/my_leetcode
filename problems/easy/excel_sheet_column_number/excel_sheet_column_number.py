import string


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 1
        suma = 0
        for j in range(-1, -len(columnTitle) - 1, -1):
            suma += (ord(columnTitle[j]) - 64) * base
            base *= 26
        return suma
