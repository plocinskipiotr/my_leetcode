class Solution:
    d = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000
         }

    e = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    def romanToInt(self, s: str) -> int:
        suma = 0
        i = 0
        while i < len(s):
            x = s[i]
            try:
                y = s[i] + s[i + 1]
                if y in Solution.e:
                    suma += Solution.e[y]
                    i += 2
                    continue
                if x in Solution.d:
                    suma += Solution.d[x]
                    i += 1
            except IndexError:
                suma += Solution.d[x]
                break

        return suma
