from unittest import TestCase
from maximum_depth_of_binary_tree import Solution, TreeNode


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
        p.right.right.right = TreeNode(6)

        lvl = s.maxDepth0(p)
        self.assertEqual(4, lvl)

    def test_is_symmetric_1(self):
        s = Solution()
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(2)

        lvl = s.maxDepth0(p)
        self.assertEqual(2, lvl)
