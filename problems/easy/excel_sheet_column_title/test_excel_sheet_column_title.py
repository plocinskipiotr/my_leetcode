from unittest import TestCase
from excel_sheet_column_title import Solution

class TestSolution(TestCase):
    def test_convert_to_title(self):
        s = Solution()
        a = s.convertToTitle(27)
        self.assertEqual('AA',a)

    def test_convert_to_title12(self):
        s = Solution()
        a = s.convertToTitle(28)
        self.assertEqual('AB', a)

    def test_convert_to_title13(self):
        s = Solution()
        a = s.convertToTitle(53)
        self.assertEqual('BA', a)

    def test_convert_to_title2(self):
        s = Solution()
        a = s.convertToTitle(26)
        self.assertEqual('Z',a)

    def test_convert_to_title33(self):
        s = Solution()
        a = s.convertToTitle(677)
        self.assertEqual('ZA',a)

    def test_convert_to_title3(self):
        s = Solution()
        a = s.convertToTitle(701)
        self.assertEqual('ZY',a)

    def test_convert_to_title4(self):
        s = Solution()
        a = s.convertToTitle(702)
        self.assertEqual('ZZ',a)

    def test_convert_to_title23(self):
        s = Solution()
        a = s.convertToTitle(18278)
        self.assertEqual('ZZZ',a)