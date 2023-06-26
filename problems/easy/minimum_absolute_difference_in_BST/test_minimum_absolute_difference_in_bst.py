from unittest import TestCase
from minimum_absolute_difference_in_bst import Solution, TreeNode


class TestSolution(TestCase):
    def test_get_minimum_difference(self):
        s = Solution()
        root = TreeNode(4)
        root.right = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        x = s.getMinimumDifference(root)
        self.assertEqual(1, x)

    def test_get_minimum_difference2(self):
        s = Solution()
        root = TreeNode(236)
        root.left = TreeNode(104)
        root.right = TreeNode(701)
        root.left.right = TreeNode(227)
        root.right.right = TreeNode(911)
        x = s.getMinimumDifference(root)
        self.assertEqual(9, x)
