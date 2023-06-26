class Solution:
    def convertToBase7(self, num: int) -> str:
        s = '' if num != 0 else '0'
        num1 = num if num > 0 else -num

        while num1:
            num1, digit = divmod(num1, 7)
            s = str(digit) + s

        return s if num >= 0 else '-' + s
