from unittest import TestCase
from binary_tree_paths import Solution,TreeNode

class TestSolution(TestCase):
    def test_binary_tree_paths(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.left.left = TreeNode(4)
        root.right = TreeNode(3)
        s = Solution()
        x = s.binaryTreePaths(root)
        print(x)

    def test_binary_tree_paths0(self):
        root = TreeNode(1)
        s = Solution()
        x = s.binaryTreePaths(root)
        print(x)

    def test_binaryTreePathsIter(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.left.left = TreeNode(4)
        root.right = TreeNode(3)
        s = Solution()
        x = s.binaryTreePathsIter(root)
        print(x)

    def test_binaryTreePathsIter0(self):
        root = TreeNode(1)
        s = Solution()
        x = s.binaryTreePathsIter(root)
        print(x)