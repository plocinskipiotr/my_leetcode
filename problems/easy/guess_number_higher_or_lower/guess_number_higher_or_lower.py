# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int, n=6) -> int:
    if num > n:
        return 1
    elif num < n:
        return -1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        mid = 1
        while l <= r:
            mid = (l + r) // 2
            g = guess(mid)
            if g == 1:
                r = mid - 1
            elif g == -1:
                l = mid + 1
            else:
                return mid

        return mid
