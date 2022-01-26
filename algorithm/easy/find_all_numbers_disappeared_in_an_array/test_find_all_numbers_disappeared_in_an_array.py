from unittest import TestCase
from find_all_numbers_disappeared_in_an_array import Solution


class TestSolution(TestCase):
    def test_find_disappeared_numbers(self):
        s = Solution()
        data = [4, 3, 2, 7, 8, 2, 3, 1]
        x = s.findDisappearedNumbers(data)
        self.assertEqual(x, [5, 6])

    def test_find_disappeared_numbers_2(self):
        s = Solution()
        data = [1, 1]
        x = s.findDisappearedNumbers(data)
        self.assertEqual(x, [2])

    def test_find_disappeared_numbers_3(self):
        s = Solution()
        data = [1]
        x = s.findDisappearedNumbers(data)
        self.assertEqual(x, [])
