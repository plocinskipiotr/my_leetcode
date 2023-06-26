class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        d = dict()
        s = s.split()
        if len(s) != len(pattern):
            return False

        for c, word in zip(pattern, s):
            if c not in d.keys() and word in d.values():
                return False
            if c not in d.keys():
                d[c] = word
            if d[c] != word:
                return False
        return True
