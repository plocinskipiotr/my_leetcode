from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:

        suma = 0
        c = Counter(s)
        for v in c.values():
            suma += (v // 2) * 2
            if suma % 2 == 0 and v % 2 == 1:
                suma += 1
        return suma
