from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if bits[i] == 0:
                if i == len(bits) - 1:
                    return True
                else:
                    i += 1
            else:
                if i == len(bits) - 2:
                    return False
                else:
                    i += 2
