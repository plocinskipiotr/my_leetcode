from unittest import TestCase
from roman_integer import Solution


class TestSolution(TestCase):
    def test_roman_to_int(self):
        data = 'I'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 1)

        data = 'II'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 2)

        data = 'III'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 3)

        data = 'IV'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 4)

        data = 'V'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 5)

        data = 'VI'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 6)

        data = 'VII'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 7)

        data = 'VIII'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 8)

        data = 'IX'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 9)

        data = 'X'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 10)

        data = 'XL'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 40)

        data = 'L'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 50)

        data = 'XC'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 90)

        data = 'C'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 100)

        data = 'CD'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 400)

        data = 'D'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 500)

        data = 'CM'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 900)

        data = 'M'
        s = Solution()
        r = s.romanToInt(data)
        self.assertEqual(r, 1000)