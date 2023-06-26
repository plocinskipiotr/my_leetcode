from unittest import TestCase
from excel_sheet_column_number import Solution


class TestSolution(TestCase):
    def test_title_to_number(self):
        s = Solution()
        x = s.titleToNumber('A')
        self.assertEqual(1, x)

    def test_title_to_number1(self):
        s = Solution()
        x = s.titleToNumber('AA')
        self.assertEqual(27, x)

    def test_title_to_number2(self):
        s = Solution()
        x = s.titleToNumber('AAA')
        self.assertEqual(703, x)

    def test_title_to_number3(self):
        s = Solution()
        x = s.titleToNumber('AB')
        self.assertEqual(28, x)