class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        if s == s[::-1]:
            return True

        while left < right:

            if s[left] != s[right]:
                left_str, right_str = s[left:right], s[left + 1:right + 1]
                return left_str == left_str[::-1] or right_str == right_str[::-1]
            left, right = left + 1, right - 1

        return True
