class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            res = mid * (mid + 1) // 2
            if res == n:
                return mid
            elif res > n:
                r = mid - 1
            else:
                l = mid + 1
        return l
