from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1, s2, s3 = {x for x in 'qwertyuiop'}, \
                     {x for x in 'asdfghjkl'}, \
                     {x for x in 'zxcvbnm'}

        return [i for i in words if s1.issuperset(i.lower()) \
                or s2.issuperset(i.lower()) \
                or s3.issuperset(i.lower())]
