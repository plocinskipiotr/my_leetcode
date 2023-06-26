from unittest import TestCase
from path_sum import Solution,TreeNode

class TestSolution(TestCase):
    def test_has_path_sum_iterative(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.right = None
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)

        s = Solution()
        x = s.hasPathSumIterative(root,22)
        self.assertTrue(x)
