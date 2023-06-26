from unittest import TestCase
from diameter_of_binary_tree import Solution, TreeNode


class TestSolution(TestCase):
    def test_traverse_tree(self):
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        x = s.diameterOfBinaryTree(root)
        self.assertEqual(2, x)

    def test_traverse_tree3(self):
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        x = s.diameterOfBinaryTree(root)
        self.assertEqual(2, x)

    def test_traverse_tree4(self):
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(10)
        root.left.left.left = TreeNode(7)
        root.left.right.right = TreeNode(15)
        x = s.diameterOfBinaryTree(root)
        self.assertEqual(4, x)
