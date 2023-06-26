from unittest import TestCase
from symmetric_tree import TreeNode
from symmetric_tree import Solution


class TestSolution(TestCase):
    def test_is_symmetric(self):
        s = Solution()
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(2)
        p.left.left = TreeNode(3)
        p.left.right = TreeNode(4)
        p.right.left = TreeNode(4)
        p.right.right = TreeNode(3)

        bool = s.isSymmetric(p)
        self.assertTrue(bool, True)

    def test_is_symmetric_1(self):
        s = Solution()
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(2)
        p.left.left = TreeNode(3)
        p.left.right = TreeNode(4)
        p.right.left = TreeNode(3)
        p.right.right = TreeNode(3)

        bool = s.isSymmetric(p)
        self.assertFalse(bool)

    def test_is_symmetric_2(self):
        s = Solution()
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(2)
        p.left.right = TreeNode(4)
        p.right.left = TreeNode(3)
        p.right.right = TreeNode(3)

        bool = s.isSymmetric(p)
        self.assertFalse(bool)
