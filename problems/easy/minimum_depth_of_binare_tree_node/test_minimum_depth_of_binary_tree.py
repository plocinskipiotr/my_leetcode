from unittest import TestCase
from minimum_depth_of_binary_tree import Solution, TreeNode

class TestSolution(TestCase):
    def test_min_depth(self):
        s = Solution()
        root = TreeNode(2)
        root.left = None
        root.right = TreeNode(3)
        root.right.left = None
        root.right.right = TreeNode(4)
        root.right.right.left = None
        root.right.right.right = TreeNode(5)
        root.right.right.right.left = None
        root.right.right.right.right = TreeNode(6)
        x = s.minDepth(root)
        self.assertEqual(x,5)
