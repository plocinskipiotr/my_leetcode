from unittest import TestCase
from n_ary_tree_preorder_traversal import Solution, Node


class TestSolution(TestCase):
    def test_preorder(self):
        s = Solution()
        root = Node(1)
        root.children = [Node(3), Node(2), Node(4)]
        root.children[0].children = [Node(5), Node(6)]
        x = s.preorder(root)
        print(x)

    def test_preorder2(self):
        s = Solution()
        root = Node(1)
        root.children = [Node(3), Node(2), Node(4)]
        root.children[0].children = [Node(5), Node(6)]
        x = s.preorder_iter(root)
        print(x)
