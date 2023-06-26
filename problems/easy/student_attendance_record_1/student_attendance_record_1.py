import re


class Solution:
    def checkRecord(self, s: str) -> bool:
        return re.fullmatch('.*A.*A.*|.*[L]{3}.*', s) is None
