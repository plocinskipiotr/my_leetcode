from unittest import TestCase
from largest_number_at_least_twice_of_others import Solution


class TestSolution(TestCase):

    def test_dominant_index_0(self):
        lst = [3, 6, 1, 0]
        s = Solution()
        result = s.dominantIndex(lst)
        self.assertEqual(1, result)

    def test_dominant_index_1(self):
        lst = [1, 2, 3, 4]
        s = Solution()
        result = s.dominantIndex(lst)
        self.assertEqual(-1, result)

    def test_dominant_index_2(self):
        lst = [1, 0]
        s = Solution()
        result = s.dominantIndex(lst)
        self.assertEqual(0, result)

    def test_dominant_index_3(self):
        lst = [1, 0, 0]
        s = Solution()
        result = s.dominantIndex(lst)
        self.assertEqual(0, result)

    def test_dominant_index_4(self):
        lst = [0,1,0]
        s = Solution()
        result = s.dominantIndex(lst)
        self.assertEqual(1, result)