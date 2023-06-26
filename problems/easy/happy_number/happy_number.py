class Solution:

    def calcNext(self, n: int) -> int:
        sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            sum += digit ** 2
        return sum

    def isHappy(self, n: int) -> bool:

        hashmap = set()
        while n != 1 and n not in hashmap:
            hashmap.add(n)
            n = self.calcNext(n)

        return n == 1

    def isHappyTurtle(self, n: int) -> bool:

        if n == 1:
            return True

        first, second = n, self.calcNext(n)

        while first != second:
            if second == 1:
                return True
            first = self.calcNext(first)
            second = self.calcNext(second)
            second = self.calcNext(second)
        return False
