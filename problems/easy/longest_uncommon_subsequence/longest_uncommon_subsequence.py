class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        if len(a) == len(b) and a != b:
            return len(a)
        if len(a) != len(b):
            return max(len(a), len(b))
