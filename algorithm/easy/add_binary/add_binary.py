class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, carry, res = -1, 0, ''
        aL, bL = -len(a), -len(b)

        while i >= min(aL, bL):
            el_a = int(a[i]) if i >= aL else 0
            el_b = int(b[i]) if i >= bL else 0
            r = (el_a + el_b + carry) % 2
            res = ''.join([str(r),res])
            carry = 1 if el_a + el_b + carry > 1 else 0
            i -= 1
        return "1" + res if carry else res
