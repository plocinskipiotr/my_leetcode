class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lenght = 0
        last_char = len(s) - 1

        for i in range(last_char, -1, -1):
            if s[i] != ' ':
                lenght += 1
            else:
                if lenght > 0:
                    return lenght
        return lenght
