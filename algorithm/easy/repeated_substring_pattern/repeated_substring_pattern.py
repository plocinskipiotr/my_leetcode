class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        j = 0
        can = s[0]
        start = 1
        end = 2
        while len(can) <= len(s) // 2:
            while can == s[start:end]:
                if end >= len(s):
                    return True
                start += len(can)
                end += len(can)
            j += 1
            can = s[:j]
            start = len(can)
            end = 2 * len(can)
        return False

    def repeatedSubstringPattern2(self, s: str) -> bool:
        j = 1
        can = s[0]
        while len(can) <= len(s) // 2:

            rep = len(s) // len(can)
            if rep * can == s:
                return True

            can = s[:j + 1]
            j += 1

        return False
