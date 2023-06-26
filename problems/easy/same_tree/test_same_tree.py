from unittest import TestCase
from same_tree import Solution, TreeNode


class TestSolution(TestCase):
    def test_is_same_tree(self):
        s = Solution()
        node_p = TreeNode(1)
        node_p.left = TreeNode(2)
        node_p.right = TreeNode(3)
        # node_p.left.left = TreeNode(4)
        # node_p.left.right = TreeNode(5)
        # node_p.right.left = TreeNode(6)
        # node_p.right.right = TreeNode(7)

        node_q = TreeNode(1)
        node_q.left = TreeNode(2)
        node_q.right = TreeNode(3)
        # node_q.left.left = TreeNode(4)
        # node_q.left.right = TreeNode(5)
        # node_q.right.left = TreeNode(6)
        # node_q.right.right = TreeNode(7)

        bool = s.isSameTree(node_p, node_q)
        self.assertTrue(bool, True)
