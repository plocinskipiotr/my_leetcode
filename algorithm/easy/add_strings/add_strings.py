class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = j = -1
        ASCI_SHIFT = 48

        if len(num1) < len(num2):
            num1, num2 = num2, num1

        res = ''
        r = 0
        while i >= -len(num1):

            num_1 = ord(num1[i]) - ASCI_SHIFT
            if i >= -len(num2):
                num_2 = ord(num2[j]) - ASCI_SHIFT
            else:
                num_2 = 0

            sum = r + num_1 + num_2
            digit = sum % 10
            if sum > 9:
                r = 1
            else:
                r = 0

            res = chr(digit + ASCI_SHIFT) + res

            i -= 1
            j -= 1

        return res if not r else '1' + res
