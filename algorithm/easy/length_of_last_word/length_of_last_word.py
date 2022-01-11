class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        l = 0
        for i in range(-1, -len(s) - 1, -1):
            if s[i] is not ' ':
                l += 1
            if l and s[i] == ' ':
                return l

        return l
