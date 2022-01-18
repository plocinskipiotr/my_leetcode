from unittest import TestCase
from binary_tree_postorder_traversal import Solution, TreeNode


class TestSolution(TestCase):
    def test_postorder_traversal(self):
        s = Solution()
        head = TreeNode(1)
        head.left = TreeNode(2)
        head.left.right = TreeNode(3)
        head.right = TreeNode(2)
        head.right.left = TreeNode(3)
        head.right.right = TreeNode(3)

        lst = s.postorderTraversal(head)
        self.assertEqual([3, 2, 3, 3, 2, 1], lst)

    def test_postorder_traversal_stack(self):
        s = Solution()
        head = TreeNode(1)
        head.left = TreeNode(2)
        head.left.right = TreeNode(3)
        head.right = TreeNode(2)
        head.right.left = TreeNode(3)
        head.right.right = TreeNode(3)

        lst = s.postorderTraversalStack(head)
        self.assertEqual([3, 2, 3, 3, 2, 1], lst)

    def test_postorder_traversal_stack2(self):
        s = Solution()
        head = TreeNode(1)

        lst = s.postorderTraversalStack(head)
        self.assertEqual([1], lst)