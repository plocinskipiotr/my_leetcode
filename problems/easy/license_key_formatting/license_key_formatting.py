class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        cnt = 0
        res = ''
        for char in s:
            if char.isalnum():
                res += char.upper()
                cnt += 1

        groups, shift = divmod(cnt, k)
        if shift == 0:
            groups -= 1
            shift = k

        i = 0
        r = res[:shift]
        while i < groups:
            r += '-' + res[shift + i * k:shift + (1 + i) * k]
            i += 1
        return r
