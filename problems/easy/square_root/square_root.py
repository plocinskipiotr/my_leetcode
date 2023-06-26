class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x // 2

        if x == 1:
            return 1

        while l <= r:

            mid = (l + r) // 2
            sq = mid * mid
            if sq == x:
                return mid

            if sq > x:
                r = mid - 1
            else:
                l = mid + 1

        return min(l, r)
