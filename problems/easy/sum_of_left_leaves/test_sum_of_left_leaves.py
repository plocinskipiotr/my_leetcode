from unittest import TestCase
from sum_of_left_leaves import Solution, TreeNode


class TestSolution(TestCase):
    def test_sum_of_left_leaves_recc(self):
        s = Solution()
        head = TreeNode(3)
        head.left = TreeNode(9)
        head.right = TreeNode(20)
        head.right.left = TreeNode(15)
        head.right.right = TreeNode(7)
        sum = s.sumOfLeftLeavesIter(head)
        self.assertEqual(24,sum)

    def test_sum_of_left_leaves_recc2(self):
        s = Solution()
        head = TreeNode(3)
        head.left = TreeNode(4)
        head.right = TreeNode(5)
        head.left.left = TreeNode(-7)
        head.left.right = TreeNode(-6)
        head.right.left = None
        head.right.right = None
        head.left.left.left = TreeNode(-7)
        head.left.left.right = None
        head.left.right.left = TreeNode(-5)
        head.left.right.left = TreeNode(-4)

        sum = s.sumOfLeftLeavesIter(head)
        self.assertEqual(-11,sum)

    def test_sum_of_left_leaves_recc3(self):
        s = Solution()
        head = TreeNode(1)
        head.left = TreeNode(2)
        head.right = TreeNode(3)
        head.left.left = TreeNode(4)
        head.left.right = TreeNode(5)
        head.right.left = TreeNode(6)
        head.right.right = TreeNode(7)

        sum = s.sumOfLeftLeavesIter(head)
        self.assertEqual(10,sum)

