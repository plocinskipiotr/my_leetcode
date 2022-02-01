from unittest import TestCase
from binary_tree_tilt import Solution, TreeNode


class TestSolution(TestCase):
    def test_find_tilt(self):
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        x = s.findTilt(root)
        self.assertEqual(1, x)

    def test_find_tilt2(self):
        s = Solution()
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(9)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(7)
        x = s.findTilt(root)
        self.assertEqual(15, x)
