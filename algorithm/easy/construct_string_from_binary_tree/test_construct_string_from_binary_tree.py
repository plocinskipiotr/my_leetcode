from unittest import TestCase
from construct_string_from_binary_tree import Solution, TreeNode


class TestSolution(TestCase):
    def test_tree2str(self):
        s = Solution()
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        x = s.tree2str(root)
        self.assertEqual('1(2(4))(3)', x)

    def test_tree2str2(self):
        s = Solution()
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.left = TreeNode(2)
        root.left.right = TreeNode(4)
        x = s.tree2str(root)
        self.assertEqual('1(2()(4))(3)', x)
