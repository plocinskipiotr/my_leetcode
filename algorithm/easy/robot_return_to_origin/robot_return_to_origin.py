from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = Counter(moves)
        return c['D'] == c['U'] and c['R'] == c['L']
        