from typing import List


class Solution:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        l, r = 0, len(letters) - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2

            if ord(letters[mid]) <= ord(target):
                l = mid + 1
            else:
                ans = letters[mid]
                r = mid - 1

        return ans if ans != -1 else letters[0]
