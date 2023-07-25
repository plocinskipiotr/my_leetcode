class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ''

        base = strs[0]
        for i in range(len(base)):
            ref_char = base[i]
            for word in strs[1:]:
                if len(word) <= i or word[i] != ref_char:
                    return base[:i]
        return base
