from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(area ** 0.5)
        l = int(area / w)

        while l * w != area:
            w -= 1
            l = int(area / w)

        return [l, w]
