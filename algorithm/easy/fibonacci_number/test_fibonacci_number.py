from unittest import TestCase
from fibonacci_number import Solution


class TestSolution(TestCase):
    def test_fib(self):
        s = Solution()
        n = 5
        x = s.fib(n)
        self.assertEqual(x, 5)

    def test_fib2(self):
        s = Solution()
        n = 6
        x = s.fib(n)
        self.assertEqual(x, 8)

    def test_fib3(self):
        s = Solution()
        n = 7
        x = s.fib(n)
        self.assertEqual(x, 13)

    def test_fib_iter(self):
        s = Solution()
        n = 5
        x = s.fib_iter(n)
        self.assertEqual(x, 5)

    def test_fib_iter2(self):
        s = Solution()
        n = 6
        x = s.fib_iter(n)
        self.assertEqual(x, 8)

    def test_fib_iter3(self):
        s = Solution()
        n = 7
        x = s.fib_iter(n)
        self.assertEqual(x, 13)
