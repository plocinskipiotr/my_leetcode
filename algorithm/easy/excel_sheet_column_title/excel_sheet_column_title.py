import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet, res, BASE = dict(), '', 26
        for i, el in enumerate(string.ascii_uppercase, start=1):
            alphabet[i] = el
        alphabet[0] = 'Z'

        while columnNumber > 0:
            mod = columnNumber % BASE
            res = alphabet[mod] + res

            if mod == 0:
                columnNumber = (columnNumber // BASE) - 1
            else:
                columnNumber //= BASE

        return res
