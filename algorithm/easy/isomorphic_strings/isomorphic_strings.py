class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = dict(), dict()

        for (s1, s2) in zip(s, t):
            if s1 in d1.keys():
                if d1.get(s1) != s2:
                    return False
            if s2 in d2.keys():
                if d2.get(s2) != s1:
                    return False

            d1[s1], d2[s2] = s2, s1
        return True
