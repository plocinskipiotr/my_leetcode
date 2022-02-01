class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        end = 2 * k
        start = end - 2 * k

        s1 = ''
        while end <= len(s):
            s1 += ''.join(reversed(s[start:start + k]))
            s1 += s[start + k:end]
            end += 2 * k
            start = end - 2 * k

        remaining = s[start:len(s)]
        if len(remaining) < k:
            s1 += ''.join(reversed(remaining))
        else:
            s1 += ''.join(reversed(remaining[:k]))
            s1 += remaining[k:]

        return s1

    def reverseStr2(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i:i + k] = reversed(a[i:i + k])
        return ''.join(a)
