from unittest import TestCase
from detect_capital import Solution


class TestSolution(TestCase):
    def test_detect_capital_use(self):
        s = Solution()
        data = 'USA'
        self.assertTrue(s.detectCapitalUseRegex(data))

    def test_detect_capital_use2(self):
        s = Solution()
        data = 'leetcode'
        self.assertTrue(s.detectCapitalUseRegex(data))

    def test_detect_capital_use3(self):
        s = Solution()
        data = 'Google'
        self.assertTrue(s.detectCapitalUseRegex(data))

    def test_detect_capital_use4(self):
        s = Solution()
        data = 'FlaG'
        self.assertFalse(s.detectCapitalUseRegex(data))

    def test_detect_capital_use5(self):
        s = Solution()
        data = "mL"
        self.assertFalse(s.detectCapitalUseRegex(data))

    def test_detect_capital_use6(self):
        s = Solution()
        data = "uZfa"
        self.assertFalse(s.detectCapitalUseRegex(data))
