import re


class Solution:

    def is_lower(self, char):
        if ord(char) > 90:
            return True
        else:
            return False

    def detectCapitalUse(self, word: str) -> bool:

        if len(word) < 2:
            return True

        lower = self.is_lower(word[0]) or not self.is_lower(word[0]) and self.is_lower(word[1])

        for i in range(1, len(word)):
            if lower:
                if not self.is_lower(word[i]):
                    return False
            else:
                if self.is_lower(word[i]):
                    return False
        return True

    def detectCapitalUseRegex(self, word: str) -> bool:
        return re.fullmatch('[A-Z]*|.[a-z]*', word) is not None
