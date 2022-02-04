from unittest import TestCase
from longest_harmonious_subsequence import Solution


class TestSolution(TestCase):
    def test_find_lhs(self):
        s = Solution()
        nums = [1, 3, 2, 2, 5, 2, 3, 7]
        d = s.findLHS(nums)
        self.assertEqual(d, 5)

    def test_find_lhs2(self):
        s = Solution()
        nums = [1,2,3,4]
        d = s.findLHS(nums)
        self.assertEqual(d, 2)

    def test_find_lhs3(self):
        s = Solution()
        nums = [1,1,1,1]
        d = s.findLHS(nums)
        self.assertEqual(d, 0)

    def test_find_lhs4(self):
        s = Solution()
        nums = [1,2,2,1]
        d = s.findLHS(nums)
        self.assertEqual(d, 4)

    def test_find_lhs5(self):
        s = Solution()
        nums = [1,3,5,7,9,11,13,15,17]
        d = s.findLHS(nums)
        self.assertEqual(d, 0)
