class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def fib_iter(self, n: int) -> int:
        sum = prev = prevprev = 0
        for i in range(n + 1):
            if i == 0:
                sum = 0
            elif i == 1:
                prevprev = 0
                prev = 1
                sum += 1
            else:
                sum = prev + prevprev
                prevprev = prev
                prev = sum
        return sum
