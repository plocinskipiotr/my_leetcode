class Solution:
    def reverseVowels(self, s: str) -> str:
        d = set((['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']))
        i, j = 0, len(s) - 1
        s = [i for i in s]

        while i < j:

            if s[i]in d and s[j] in d:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

            if s[i] not in d:
                i += 1

            if s[j] not in d:
                j -= 1

        return ''.join(s)
