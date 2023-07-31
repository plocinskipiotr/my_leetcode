from unittest import TestCase

from problems.easy.search_insert_position.src.search_insert_position import Solution


class TestSolution(TestCase):
    def test_search_insert_0(self):
        s = Solution()
        data = []
        i = s.searchInsert(data, 5)
        self.assertEqual(0, i)

    def test_search_insert_1(self):
        s = Solution()
        data = [1, 3, 5, 6]
        i = s.searchInsert(data, 5)
        self.assertEqual(2, i)

    def test_search_insert_2(self):
        s = Solution()
        data = [1, 3, 5, 6]
        i = s.searchInsert(data, 2)
        self.assertEqual(1, i)

    def test_search_insert_3(self):
        s = Solution()
        data = [1, 3, 5, 6]
        i = s.searchInsert(data, 6)
        self.assertEqual(3, i)

    def test_search_insert_4(self):
        s = Solution()
        data = [1, 3, 5, 6]
        i = s.searchInsert(data, 7)
        self.assertEqual(4, i)
