from unittest import TestCase

from remove_duplicates_from_sorted_array import Solution


class TestSolution(TestCase):
    def test_remove_duplicates_0(self):
        s = Solution()
        data = []
        x = s.removeDuplicates3(data)
        self.assertEqual(x, 0)

    def test_remove_duplicates_1(self):
        s = Solution()
        data = [1, 1, 1, 3, 3, 3, 5, 5, 5, 7, 7, 7]
        x = s.removeDuplicates3(data)
        self.assertEqual(x, 4)

    def test_remove_duplicates_2(self):
        s = Solution()
        data = [1]
        x = s.removeDuplicates3(data)
        self.assertEqual(x, 1)

    def test_remove_duplicates_3(self):
        s = Solution()
        data = [1, 2, 3, 4, 5, 6]
        x = s.removeDuplicates3(data)
        self.assertEqual(x, 6)

    def test_remove_duplicates_4(self):
        s = Solution()
        data = [1,1,2]
        x = s.removeDuplicates3(data)
        self.assertEqual(x, 2)

    def test_remove_duplicates_5(self):
        s = Solution()
        data = [0,0,1,1,1,2,2,3,3,4]
        x = s.removeDuplicates3(data)
        self.assertEqual(x, 5)

    def test_remove_duplicates_6(self):
        s = Solution()
        data = [1,2]
        x = s.removeDuplicates3(data)
        self.assertEqual(x, 2)
