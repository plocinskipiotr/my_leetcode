from unittest import TestCase
from average_of_levels_in_binary_tree import Solution, TreeNode


class TestSolution(TestCase):
    def test_average_of_levels(self):
        s = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        x = s.averageOfLevelsIter(root)
        self.assertEqual([3.00000, 14.50000, 11.00000], x)

    def test_average_of_levels2(self):
        s = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.left.left = TreeNode(15)
        root.left.right = TreeNode(7)
        x = s.averageOfLevels(root)
        self.assertEqual([3.00000, 14.50000, 11.00000], x)
