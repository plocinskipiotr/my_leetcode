from unittest import TestCase
from binary_tree_preorder_traversal import Solution, TreeNode


class TestSolution(TestCase):
    def test_preorder_traversal(self):
        s = Solution()
        head = TreeNode(1)
        head.left = TreeNode(2)
        head.left.right = TreeNode(3)
        head.right = TreeNode(2)
        head.right.left = TreeNode(3)
        head.right.right = TreeNode(3)

        lst = s.preorderTraversalStack(head)
        self.assertEqual([1, 2, 3, 2, 3, 3], lst)
