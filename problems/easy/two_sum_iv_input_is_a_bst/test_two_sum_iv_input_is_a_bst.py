from unittest import TestCase
from two_sum_iv_input_is_a_bst import Solution, TreeNode


class TestSolution(TestCase):
    def test_find_target2(self):
        s = Solution()
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.left.left = TreeNode(2)
        root.right = TreeNode(6)
        root.right.right = TreeNode(7)
        x = s.findTarget2(root, 12)
        self.assertTrue(x)

    def test_find_target3(self):
        s = Solution()
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.right = TreeNode(7)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(8)
        x = s.findTarget2(root, 9)
        self.assertTrue(x)
