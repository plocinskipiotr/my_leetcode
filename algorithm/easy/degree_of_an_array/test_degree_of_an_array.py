from unittest import TestCase
from degree_of_an_array import Solution


class TestSolution(TestCase):
    def test_find_shortest_sub_array(self):
        s = Solution()
        nums = [1, 2, 2, 3, 1]
        x = s.findShortestSubArray(nums)
        self.assertEqual(2, x)

    def test_find_shortest_sub_array2(self):
        s = Solution()
        nums = [1]
        x = s.findShortestSubArray(nums)
        self.assertEqual(1, x)

    def test_find_shortest_sub_array3(self):
        s = Solution()
        nums = [2,1]
        x = s.findShortestSubArray(nums)
        self.assertEqual(1, x)
