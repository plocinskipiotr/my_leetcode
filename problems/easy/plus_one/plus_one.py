class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        for i in range(len(digits)):
            if len(digits) - i == 1 and digits[0] == 9:
                prefix = 1
                digits[0] = 0
                return [prefix, *digits]
            if digits[len(digits) - i - 1] == 9:
                digits[len(digits) - i - 1] = 0
            else:
                digits[len(digits) - i - 1] = digits[len(digits) - i - 1] + 1
                return digits
