from unittest import TestCase
from longest_continous_increasing_subsequence import Solution


class TestSolution(TestCase):
    def test_find_length_of_lcis(self):
        s = Solution()
        data = [1, 3, 5, 4, 7]
        x = s.findLengthOfLCIS(data)
        self.assertEqual(3, x)

    def test_find_length_of_lcis2(self):
        s = Solution()
        data = [2, 2, 2, 2, 2]
        x = s.findLengthOfLCIS(data)
        self.assertEqual(1, x)

    def test_find_length_of_lcis3(self):
        s = Solution()
        data = [1, 2]
        x = s.findLengthOfLCIS(data)
        self.assertEqual(2, x)

    def test_find_length_of_lcis4(self):
        s = Solution()
        data = [1]
        x = s.findLengthOfLCIS(data)
        self.assertEqual(1, x)