from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1

        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
