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
