class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = str(x)
        p = len(lst) // 2
        if len(lst) % 2:
            a = lst[:p + 1]
            b = lst[p:]
        else:
            a = lst[:p]
            b = lst[p:]

        return a == b[::-1]

    def is_palindrome_numerical(self, x: int) -> bool:

        if x < 0 or x % 10 == 0 and x != 0:
            return False

        reversed_num = 0
        while x > reversed_num:
            a = x % 10
            reversed_num = reversed_num * 10 + a
            x //= 10

        if x == reversed_num or x == reversed_num // 10:
            return True
