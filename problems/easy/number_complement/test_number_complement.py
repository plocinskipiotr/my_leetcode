from unittest import TestCase
from number_complement import Solution


class TestSolution(TestCase):
    def test_find_complement(self):
        s = Solution()
        data = 1
        x = s.findComplementXOR(data)
        self.assertEqual(x, 0)

    def test_find_complement1(self):
        s = Solution()
        data = 2
        x = s.findComplementXOR(data)
        self.assertEqual(x, 1)

    def test_find_complement2(self):
        s = Solution()
        data = 3
        x = s.findComplementXOR(data)
        self.assertEqual(x, 0)

    def test_find_complement3(self):
        s = Solution()
        data = 4
        x = s.findComplementXOR(data)
        self.assertEqual(x, 3)

    def test_find_complement4(self):
        s = Solution()
        data = 5
        x = s.findComplementXOR(data)
        self.assertEqual(x, 2)

    def test_find_complement5(self):
        s = Solution()
        data = 6
        x = s.findComplementXOR(data)
        self.assertEqual(x, 1)

    def test_find_complement6(self):
        s = Solution()
        data = 7
        x = s.findComplementXOR(data)
        self.assertEqual(x, 0)

    def test_find_complement7(self):
        s = Solution()
        data = 8
        x = s.findComplementXOR(data)
        self.assertEqual(x, 7)

    def test_find_complement8(self):
        s = Solution()
        data = 9
        x = s.findComplementXOR(data)
        self.assertEqual(x, 6)
