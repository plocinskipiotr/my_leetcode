class Solution:
    def addDigits(self, num: int) -> int:
        suma = num

        while suma > 9:

            digit_sum = 0
            while suma:
                digit_sum += suma % 10
                suma //= 10
            suma = digit_sum

        return suma
