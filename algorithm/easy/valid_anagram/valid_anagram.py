from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        if c1 == c2:
            return True

    def isAnagramdict(self, s: str, t: str) -> bool:
        ds, dt = dict(), dict()
        if len(s) != len(t):
            return False

        for char_s, char_t in zip(s, t):
            if char_s in ds:
                ds[char_s] += 1
            else:
                ds[char_s] = 1
            if char_t in dt:
                dt[char_t] += 1
            else:
                dt[char_t] = 1

        return ds == dt

    def isAngramsort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)