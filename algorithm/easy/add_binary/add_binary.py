class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        i = 0
        r = 0
        c = ''

        while a[i] and b[i]:
            int_a = int(a[i])
            int_b = int(b[i])

            if int_a + int_b + r == 0:
                c[i], r = 0, 0
            if int_a + int_b + r == 1:
                c[i], r = 1, 0
            if int_a + int_b + r == 2:
                c[i], r = 0, 1
            if int_a + int_b + r == 3:
                c[i], r = 1, 1

            i += 1

        long = max(a,b)

        while long[i] and r:
            int_long = int(long[i])
            if int_long + r == 1:
                c[i] = 1
                return c
            if int_long + r == 2:

