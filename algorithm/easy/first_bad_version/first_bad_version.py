# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version > 4:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:

            mid = (l + r) // 2

            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid

            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
