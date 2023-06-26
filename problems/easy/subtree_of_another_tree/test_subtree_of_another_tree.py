from unittest import TestCase
from subtree_of_another_tree import Solution, TreeNode


class TestSolution(TestCase):
    def test_is_subtree(self):
        s = Solution()
        subroot = TreeNode(4)
        subroot.left = TreeNode(1)
        subroot.right = TreeNode(2)
        x = s.mapTree(subroot)
        print(x)
        # root = TreeNode(3)
        # root.right = TreeNode(5)
        # root.left = TreeNode(4)
        # root.left.right = TreeNode(2)
        # root.left.left = TreeNode(1)
        # y = s.isSubtree(root, subroot)
        # print(y)

    def test_is_subtree2(self):
        s = Solution()
        subroot = TreeNode(4)
        subroot.left = None
        subroot.right = TreeNode(5)
        x = s.mapTree(subroot)
        print(x)
