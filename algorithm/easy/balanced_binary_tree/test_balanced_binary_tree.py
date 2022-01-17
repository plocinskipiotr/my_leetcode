from unittest import TestCase
from balanced_binary_tree import Solution,TreeNode


class TestSolution(TestCase):
    def test_bt_h(self):
        node = TreeNode(1)
        node.left = TreeNode(2)
        node.left.left = TreeNode(3)
        node.left.left.left = TreeNode(5)
        node.left.left.left = TreeNode(10)
        node.left.left.right = TreeNode(12)
        # node.left.left = TreeNode(2)
        # node.left.right = None
        # node.right.left = None
        # node.right.right = TreeNode(3)
        # node.left.left.left = TreeNode(4)
        # node.left.left.right = None
        # node.right.right.left = None
        # node.right.right.right = TreeNode(4)


        s = Solution()
        x = s.isBalanced(node)
        self.assertFalse(x)

