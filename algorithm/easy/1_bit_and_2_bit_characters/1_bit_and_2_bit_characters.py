from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-2:] == [1, 0]:
            return False
        if bits[-2:] == [0, 0]:
            return True
        if bits[-2:] == [1, 0]:
            return True
