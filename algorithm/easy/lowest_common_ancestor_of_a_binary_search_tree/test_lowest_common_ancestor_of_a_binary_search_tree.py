from unittest import TestCase
from lowest_common_ancestor_of_a_binary_search_tree import Solution
from lowest_common_ancestor_of_a_binary_search_tree import TreeNode


class TestSolution(TestCase):
    def test_lowest_common_ancestor(self):
        s = Solution()
        n = TreeNode(6)
        n.left = TreeNode(2)
        n.left.left = TreeNode(0)
        n.left.right = TreeNode(4)
        n.left.right.left = TreeNode(3)
        n.left.right.right = TreeNode(5)
        n.right = TreeNode(8)
        n.right.left = TreeNode(7)
        n.right.right = TreeNode(9)
        r = s.lowestCommonAncestorreccurence(n, TreeNode(3), TreeNode(5))
        print(r)