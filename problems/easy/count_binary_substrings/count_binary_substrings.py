class Solution:

    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        j = 1
        suma = 0
        while j < len(s) and s[j] == s[j - 1]:
            j += 1

        transition_point = j
        j += 1

        while j < len(s):

            if s[j] != s[j - 1]:
                suma += min(s[i:j].count('0'), s[i:j].count('1'))
                i = transition_point
                transition_point = j

            j += 1

        suma += min(s[i:j].count('0'), s[i:j].count('1'))

        return suma

    def countBinarySubstrings2(self, s: str) -> int:

        zeros = ones = suma = 0
        act_car = s[0]
        first_seq = True

        for char in s:
            if char != act_car:
                act_car = char

                if first_seq:
                    first_seq = False
                else:
                    suma += min(zeros, ones)
                    if act_car == '0':
                        zeros = 0
                    else:
                        ones = 0

            zeros = zeros + 1 if char == '0' else zeros
            ones = ones + 1 if char == '1' else ones

        suma += min(zeros, ones)
        return suma
