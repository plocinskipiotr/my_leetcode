from unittest import TestCase
from summary_ranges import Solution


class TestSolution(TestCase):
    def test_summary_ranges(self):
        l = [1, 2, 3, 4, 5]
        s = Solution()
        x = s.summaryRanges(l)
        print(x)

    def test_summary_ranges2(self):
        l = [0, 2, 3, 6, 7, 10]
        s = Solution()
        x = s.summaryRanges(l)
        print(x)

    def test_summary_ranges3(self):
        l = [0, 2, 3, 4, 6, 8, 9]
        s = Solution()
        x = s.summaryRanges(l)
        print(x)

    def test_summary_ranges4(self):
        l = [0]
        s = Solution()
        x = s.summaryRanges(l)
        print(x)
