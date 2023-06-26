class Solution:
    def countSegments(self, s: str) -> int:

        if not s:
            return 0

        cnt = 1 if s[0] != ' ' else 0
        for i in range(1, len(s) - 1):
            if s[i] == ' ' and s[i + 1] != ' ':
                cnt += 1

        return cnt
