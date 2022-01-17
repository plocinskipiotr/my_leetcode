from unittest import TestCase
from convert_sorted_array_to_binary_search_tree import Solution


class TestSolution(TestCase):
    def test_sorted_array_to_bst(self):
        s = Solution()
        array = [-10, -3, 0, 5, 9]
        tree = s.sortedArrayToBST2(array)
        print('xD')

        # array2 = [-1,0,1,2]
        # tree2 = s.sortedArrayToBST2(array2)
        # print('xD')