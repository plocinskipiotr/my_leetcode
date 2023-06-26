from unittest import TestCase
from find_mode_in_binary_search_tree import Solution, TreeNode


class TestSolution(TestCase):
    def test_find_mode(self):
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(2)
        root.right.right.right = TreeNode(2)
        root.right.right.right.left = TreeNode(3)
        root.right.right.right.right = TreeNode(3)
        x = s.findMode(root)
        self.assertEqual([1, 2], x)
