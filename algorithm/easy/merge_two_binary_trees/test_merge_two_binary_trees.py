from unittest import TestCase
from merge_two_binary_trees import Solution, TreeNode


class TestSolution(TestCase):
    def test_merge_trees(self):
        s = Solution()
        root1 = TreeNode(1)
        root1.left = TreeNode(3)
        root1.left.left = TreeNode(5)
        root1.right = TreeNode(2)

        root2 = TreeNode(2)
        root2.left = TreeNode(1)
        root2.left.right = TreeNode(4)
        root2.right = TreeNode(3)
        root2.right.right = TreeNode(7)

        x = s.mergeTreesReccur(root1, root2)
        print(x)
